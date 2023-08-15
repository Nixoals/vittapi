import smbus
import time

bus = smbus.SMBus(1)
LCD_ADDRESS = 0x3E

class LCD1602:

    def __init__(self):
        self.__lcd_init()

    def __lcd_init(self):
        self.write_command(0x38)  # Mode 8 bits, 2 lignes, caractères 5x8
        self.write_command(0x0C)  # Écran allumé, curseur éteint
        self.write_command(0x01)  # Efface l'écran

    def write_command(self, cmd):
        bus.write_byte_data(LCD_ADDRESS, 0x80, cmd)
        time.sleep(0.05)

    def write_data(self, data):
        bus.write_byte_data(LCD_ADDRESS, 0x40, data)
        time.sleep(0.05)
    
    def write_string(self, s):
        for char in s:
            self.write_data(ord(char))

    def clear(self):
        self.write_command(0x01)  # Efface l'écran

    def set_cursor_position(self, line, position):
        # Les adresses RAM pour les lignes du LCD1602 sont généralement:
        # 1ère ligne : 0x80 + position
        # 2ème ligne : 0xC0 + position
        if line == 1:
            address = 0x80 + position
        elif line == 2:
            address = 0xC0 + position
        else:
            raise ValueError("Line number should be 1 or 2")
        
        self.write_command(address)

    def turn_on_cursor(self):
        self.write_command(0x0E)  # Allume le curseur

    def turn_off_cursor(self):
        self.write_command(0x0C)  # Éteint le curseur

    def blink_cursor(self):
        self.write_command(0x0F)  # Fait clignoter le curseur



