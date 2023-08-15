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

    def write_string(self, s, line=None):
        if line:
            pass
        else:
        # Si la longueur de la chaîne est supérieure à 16 et que la ligne n'est pas spécifiée, divisez-la en deux
            if len(s) > 16:
                first_line = s[:16]
                second_line = s[16:32]  # Prendre jusqu'à 32 caractères au total
            else:
                first_line = s
                second_line = ""

            # Écrire la première ligne
            byte_list1 = [ord(char) for char in first_line]
            bus.write_i2c_block_data(LCD_ADDRESS, 0x40, byte_list1)
            time.sleep(0.05)  # Donner un peu de temps pour l'affichage

            # Si nous avons une deuxième ligne à afficher
            if second_line:
                # Déplacez le curseur vers le début de la deuxième ligne.
                # Habituellement, l'adresse 0xC0 est utilisée pour la deuxième ligne des écrans LCD 16x2.
                self.write_command(0xC0)

                byte_list2 = [ord(char) for char in second_line]
                bus.write_i2c_block_data(LCD_ADDRESS, 0x40, byte_list2)

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
