import time
from machine import Pin, I2C
import sh1106  # Stelle sicher, dass diese Bibliothek vorhanden ist

# Initiale Ränder
xMax = 122
yMax = 58
xMin = 0
yMin = 0

# I²C initialisieren
i2c = I2C(0, sda=Pin(4), scl=Pin(5))
oled = sh1106.SH1106_I2C(128, 64, i2c)

# OLED-Display initialisieren
oled.fill(0)
oled.show()

# Zeichne immer enger werdendes Rechteck
while xMin < xMax and yMin < yMax:
    # Oberer Rand
    for i in range(xMin, xMax + 1):
        oled.pixel(i, yMin, 1)
        oled.show()

    # Rechter Rand
    for i in range(yMin, yMax + 1):
        oled.pixel(xMax, i, 1)
        oled.show()

    # Unterer Rand
    for i in range(xMax, xMin - 1, -1):
        oled.pixel(i, yMax, 1)
        oled.show()

    # Linker Rand
    for i in range(yMax, yMin - 1, -1):
        oled.pixel(xMin, i, 1)
        oled.show()
     
    # Verkleinere das Rechteck
    xMax -= 1
    yMax -= 1
    xMin += 1
    yMin += 1

# Fertig, Bildschirm leeren
oled.fill(0)
oled.show()
