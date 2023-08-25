import io
import base64
from picamera2 import Picamera2, Preview
import time


class Camera(object):
    def __init__(self):
        self.camera = Picamera2()
        self.camera_config = self.camera.create_preview_configuration()
        self.camera.configure(self.camera_config)
        #self.camera.start_preview(Preview.DRM)

    
    def get_frame(self):
        self.camera.start()
        time.sleep(2)
        data = io.BytesIO()
        image = self.camera.capture_file(data, format='jpeg')
        return base64.b64encode(image).decode()

