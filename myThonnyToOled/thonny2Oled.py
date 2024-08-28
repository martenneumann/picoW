import time
from machine import Pin, I2C
import sh1106  # Stelle sicher, dass diese Bibliothek vorhand

hoeheZeile = 10
zeile = 0

# I²C initialisieren
i2c = I2C(0, sda=Pin(4), scl=Pin(5))
oled = sh1106.SH1106_I2C(128, 64, i2c)

# Hiermit botschaften auf Oled schreiben
def display_message(message, zeile=0):
    oled.text(message, 0, (zeile * hoeheZeile))
    oled.show()
  
def display_loeschen() :  
    oled.fill(0)
    oled.show()    

while True:
    # Eingabe vom Benutzer erfassen
    eingabe = input("Gib etwas ein: ")
    
    if eingabe == "def" or zeile == 6:
        display_loeschen()
        zeile = 0;
        if eingabe == "def" : continue
        
    # Eingabe zurückgeben
    print("Du hast eingegeben:", eingabe)
    display_message(eingabe, zeile)
    zeile += 1
    
