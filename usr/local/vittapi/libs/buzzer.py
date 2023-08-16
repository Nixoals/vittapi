import time
import RPi.GPIO as GPIO


class GroveBuzzer(object):
    def __init__(self, pin):
        self.pin = pin
        self.tone = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = None
    
    def cleanup(self):
        GPIO.cleanup()

    def pitch(self, tone, duration=0.5):
        self.tone = tone
        if self.pwm:
            self.pwm.stop()
            self.pwm = None
        self.pwm = GPIO.PWM(self.pin, self.tone)
        self.pwm.ChangeFrequency(self.tone)
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