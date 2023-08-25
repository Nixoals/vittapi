import io
import base64
from picamera2 import Picamera2, Preview
import time
import os



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
        image = self.camera.capture_buffer()
        self.camera.stop()
        image_base64 = base64.b64encode(image)
        print(f"###BEGIN_IMAGE###\n{image_base64}\n###END_IMAGE###")
        return None

