import io
import base64
from picamera2 import Picamera2, Preview


class Camera(object):
    def __init__(self):
        self.camera = Picamera2()
    
    def get_frame(self):
        image = self.camera.capture_file('image.jpg')
        return base64.b64encode(image).decode()

