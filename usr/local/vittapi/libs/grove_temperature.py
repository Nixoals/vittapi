import math
import time
from grove.adc import ADC

class ADC():
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    def read(self):
        value = self.adc.read(self.channel)

        return value
        


# def main():
#     sensor = GroveTemperature(2)

#     while True:
#         adc_value = sensor.adc.read(sensor.channel)
#         resistance = (float)(1023 - adc_value) * 10000 / adc_value
        
#         print("Valeur ADC : ", adc_value)
#         print("Résistance : ", resistance)
        
#         temperature = sensor.read()
#         print("Température : {:.2f} C".format(temperature))
#         time.sleep(1)