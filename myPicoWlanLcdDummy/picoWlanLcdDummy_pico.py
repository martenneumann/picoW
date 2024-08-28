# @date 2024-08-28
# Empfange Daten vom PC und stelle sie auf OLED da
# sh1106 bib von robert-hh : https://github.com/robert-hh/SH1106
# PC prg heißt picoWlanLcdDummy_pc
# ACHTUNG: PicoW braucht wohl 2,4GHz !!!

import network
import socket
from machine import Pin, I2C
import time
import sh1106  # Stelle sicher, dass diese Bibliothek vorhanden ist

#-----------------------------------------------------------------------------------
# CONF

# WLAN-Verbindung herstellen
ssid = "my2,4GHz"  # Ersetze dies durch die SSID des 2,4 GHz Netzwerks
password = "05226091438051783374"  # Ersetze dies durch das WLAN-Passwort

# WLAN-Verbindung herstellen
#ssid = "iPhone von Marten"  # Ersetze dies durch die SSID des 2,4 GHz Netzwerks
#password = "123456789"  # Ersetze dies durch das WLAN-Passwort

sdaPin = 4
sclPin = 5
hoeheZeile = 10
#-----------------------------------------------------------------------------------

# I²C initialisieren
i2c = I2C(0, sda=Pin(sdaPin), scl=Pin(sclPin))
oled = sh1106.SH1106_I2C(128, 64, i2c)

# OLED-Display initialisieren
oled.fill(0)
oled.show()

# Hiermit botschaften auf Oled schreiben
def display_message(message, zeile=0):
    if zeile == 0 :
        oled.fill(0)
    oled.text(message, 0, (zeile * hoeheZeile))
    oled.show()
display_message('Verbinde WLAN...')
time.sleep(3)

#Onboard LED
led = Pin("LED", Pin.OUT)

#WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print('Verbinde WLAN...' ,1)
while not wlan.isconnected():
    time.sleep(1)

print('WLAN verbunden:', wlan.ifconfig())
display_message('WLAN verbunden', 1)
time.sleep(3)

# Server einrichten
addr = socket.getaddrinfo('0.0.0.0', 1234)[0][-1]
sock = socket.socket()
sock.bind(addr)
sock.listen(1)
    
print('Warte auf PC Verbindung...')
display_message('Warte auf PC ...',2)

while True:
    conn, addr = sock.accept()
    print('Verbindung von', addr)
    display_message('PC verbuden', 3)
    
    while True:
        data = conn.recv(1024)
        if not data:
            break
                
        command = data.decode().strip().upper()
        if command == 'X':
            print('Socket auf PC geschlossen')
            display_message('Socket zuuuu')
            
        elif command == 'AN':    
            led.value(1)
            print('LED an')
            display_message('LED an')
        elif command == 'AUS':
            led.value(0)
            print('LED aus')
            display_message('LED aus')
        elif command == 'BLINK':
            print('LED blinkt')
            display_message('LED blinkt')
            for _ in range(5):  # Blinkt 5 Mal
                led.toggle()
                time.sleep(0.5)
            led.value(0)
            
        else :
            print(command)
            display_message(command)            

    conn.close()
