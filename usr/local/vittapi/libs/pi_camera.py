import io
import base64
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
import time
import os
import shutil


class Camera(object):
    def __init__(self, mode=1):
        self.camera = Picamera2()
        self.camera_config = self.camera.create_preview_configuration({"size": (640, 480)}, raw=self.camera.sensor_modes[mode])
        self.camera.configure(self.camera_config)
        self.video_config = self.camera.create_video_configuration()
        self.encoder = H264Encoder(bitrate=10000000)
        # self.camera.start_preview(Preview.DRM)

    def get_frame(self):
        self.camera.start()
        time.sleep(2)
        
        # Enregistrez l'image dans le répertoire temporaire
        temp_filename = "temp_image.jpg"
        self.camera.capture_file(temp_filename)
        
        self.camera.stop()
        time.sleep(2)

        # Définir le chemin du répertoire et du fichier de destination
        filename = "image.jpg"
        dirpath = '/home/pi/Desktop/vittapi/usr/local/vittapi/app/static/images/'
        
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

    def get_record(self, duration=5):
        self.camera.start_recording(self.encoder, 'temp_video.h264')
        time.sleep(duration)
        self.camera.stop_recording()

        time.sleep(2)

        # Enregistrez la vidéo dans le répertoire temporaire
        temp_filename = "temp_video.h264"

        # Définir le chemin du répertoire et du fichier de destination
        filename = "video.h264"
        dirpath = '/home/pi/Desktop/vittapi/usr/local/vittapi/app/static/videos/'

        # Créer le répertoire s'il n'existe pas
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)

        destpath = os.path.join(dirpath, filename)

        # Copier la vidéo dans le répertoire de destination
        shutil.copy(temp_filename, destpath)

        # Supprimer la vidéo temporaire si nécessaire
        os.remove(temp_filename)


        print("VIDEO_CAPTURED_SUCCESSFULLY")
        return "VIDEO_CAPTURED_SUCCESSFULLY"