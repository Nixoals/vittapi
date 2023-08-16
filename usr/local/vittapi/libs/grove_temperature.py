import math
import time
from grove.adc import ADC

class GroveTemperature:
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    def read(self, unit='c'):
        value = self.adc.read(self.channel)
        resistance = (float)(1023 - value) * 10000 / value
        
        # Coefficients pour le thermistor NTC 10K
        A = 1.009249522e-03
        B = 2.378405444e-04
        C = 2.019202697e-07
        
        # Calculez la température en Kelvin
        temperature_in_kelvin = 1 / (A + B * math.log(resistance) + C * math.pow(math.log(resistance), 3))
        
        # Convertir en degrés Celsius
        temperature = temperature_in_kelvin - 273.15
        if unit.lower() == 'fahrenheit':
            temperature = temperature * 1.8 + 32
        elif unit.lower() == 'kelvin':
            temperature = temperature_in_kelvin
        return temperature


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