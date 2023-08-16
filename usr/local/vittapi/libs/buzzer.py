import time
import RPi.GPIO as GPIO

# Configuration
# GPIO.setmode(GPIO.BCM)
# BUZZER_PIN = 12
# GPIO.setup(BUZZER_PIN, GPIO.OUT)

# # Définir les fréquences pour DO, RE, MI, etc.
# chords_freq = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]  # C, D, E, F, G, A, B
  # Initialisation avec la fréquence DO

class GroveBuzzer(object):
    def __init__(self, pin):
        self.pin = pin
        self.tone = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.tone)
    
    def cleanup(self):
        GPIO.cleanup()

    def pitch(self, tone, duration=0.5):
        self.tone = tone
        self.pwm.ChangeFrequency(chords_freq[self.tone])
        self.pwm.start(50)
        time.sleep(duration)
        self.pwm.stop()
        self.cleanup()




# def main():
#     print("Insert Grove-Buzzer to Grove-Base-Hat slot PWM[12 13 VCC GND]")
#     print("Playing sound...")

#     for freq in chords_freq:
#         pwm.ChangeFrequency(freq)  # Change la fréquence
#         pwm.start(50)  # Démarrer la PWM avec un rapport cyclique de 50%
#         time.sleep(0.5)  # Jouer chaque note pendant une demi-seconde
#         pwm.stop()
#         time.sleep(0.1)  # Pause entre les notes

#     print("exiting application")

#     # Cleanup
#     GPIO.cleanup()

# if __name__ == '__main__':
#     main()