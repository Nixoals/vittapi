from flask import Flask, request, jsonify, Response, send_file
from flask_socketio import SocketIO, send
from flask_cors import CORS
import tempfile
import subprocess
import sys
import logging
import os
import io
import base64
import picamera

libs_directory = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '..', 'libs')
sys.path.append(libs_directory)

socketio_logger = logging.getLogger('socketio')
socketio_logger.setLevel(logging.ERROR)

engineio_logger = logging.getLogger('engineio')
engineio_logger.setLevel(logging.ERROR)

app = Flask(__name__)

precode = """
import sys
import os
import logging

logging.getLogger("root").setLevel(logging.ERROR)

libs_directory = '/usr/local/vittapi/libs'
#to remove when building package
libs_headless_directory = '/home/pi/Desktop/vittapi/usr/local/vittapi/libs'
sys.path.append(libs_directory)
sys.path.append(libs_headless_directory)

class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)
"""

CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

current_process = None


def terminate_current_process():
    global current_process
    if current_process:
        try:
            current_process.terminate()
            current_process.wait()  # Wait for the process to terminate
        except Exception as e:
            print(f"Error while terminating process: {e}")


def stream_process_output(process):
    # Capture stdout
    in_image_block = False
    image_data = []
    for line in iter(process.stdout.readline, ''):
        if "###BEGIN_IMAGE###" in line:
            in_image_block = True
            continue
        if "###END_IMAGE###" in line:
            in_image_block = False
            # Traitez ou envoyez image_data ici, qui contient votre image en base64
            image_base64 = ''.join(image_data)
            # Vous pourriez vouloir envelopper ceci dans un objet JSON ou dans une autre structure pour que le frontend puisse l'identifier
            yield f"CODE_IMAGE_DATA:{image_base64}\nEND_CODE_IMAGE_DATA\n"
            image_data = []
            continue
        if in_image_block:
            image_data.append(line.strip())
            continue
        yield line

    # Capture stderr
    for line in iter(process.stderr.readline, ''):
        yield line

    process.stdout.close()
    process.stderr.close()
    process.wait()


@app.route('/send-command', methods=['POST'])
def home_command():
    global current_process

    # Terminate any previous processes
    terminate_current_process()

    code = precode + '\n\r' + request.form.get('command')
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp:
        temp.write(code.encode())
        temp.flush()  # Make sure the data is written to the file

    current_process = subprocess.Popen(
        [sys.executable, temp.name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    return Response(stream_process_output(current_process), content_type='text/plain')


@app.route('/get-picam-image', methods=['get'])
def pi_cam_image():
    image_data = open("image.jpg", "rb").read()  # Remplacez ceci par la manière dont vous obtenez vos données d'image
    return send_file(
        io.BytesIO(image_data),
        mimetype='image/jpeg',
        as_attachment=True,
        attachment_filename='image.jpg'
    )

@app.route('/terminate', methods=['POST'])
def terminate():
    terminate_current_process()
    return Response("Process terminated", content_type='text/plain')


@socketio.on('message')
def handle_connection(data):
    if 'connection request' in data["data"]:
        send('connected')


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0")
