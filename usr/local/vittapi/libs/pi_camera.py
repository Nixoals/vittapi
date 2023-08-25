import io
import base64
from picamera2 import Picamera2, Preview
import time
import os
import shutil


class Camera(object):
    def __init__(self):
        self.camera = Picamera2()
        self.camera_config = self.camera.create_preview_configuration()
        self.camera.configure(self.camera_config)
        # self.camera.start_preview(Preview.DRM)

    def get_frame(self):
        self.camera.start()
        time.sleep(2)
        
        # Enregistrez l'image dans le répertoire temporaire
        temp_filename = "temp_image.jpg"
        self.camera.capture_image(temp_filename)
        
        self.camera.stop()
        time.sleep(2)

        # Définir le chemin du répertoire et du fichier de destination
        filename = "image.jpg"
        dirpath = '/home/pi/Desktop/vittapi/usr/local/vittapi/app/image'
        
        # Créer le répertoire s'il n'existe pas
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)

        destpath = os.path.join(dirpath, filename)

        # Copier l'image dans le répertoire de destination
        shutil.copy(temp_filename, destpath)

        # Supprimer l'image temporaire si nécessaire
        os.remove(temp_filename)

        print("IMAGE_CAPTURED_SUCCESSFULLY")
        return "IMAGE_CAPTURED_SUCCESSFULLY"
