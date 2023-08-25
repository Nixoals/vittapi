import io
import base64
from picamera import PiCamera


class Camera(object):
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 24
        self.stream = io.BytesIO()
    
    def get_frame(self):
        self.camera.capture(self.stream, 'jpeg')
        self.stream.seek(0)
        image_data = self.stream.read()
        return base64.b64encode(image_data).decode()

