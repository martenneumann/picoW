import network
import socket
from machine import Pin, I2C
import time
import sh1106  # Stelle sicher, dass diese Bibliothek vorhanden ist

# WLAN-Verbindung herstellen
ssid = "my2,4GHz"  # Ersetze dies durch die SSID des 2,4 GHz Netzwerks
password = "05226091438051783374"  # Ersetze dies durch das WLAN-Passwort

# WLAN-Verbindung herstellen
#ssid = "iPhone von Marten"  # Ersetze dies durch die SSID des 2,4 GHz Netzwerks
#password = "123456789"  # Ersetze dies durch das WLAN-Passwort


led = Pin("LED", Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print('Verbinde mit WLAN...')
while not wlan.isconnected():
    time.sleep(1)

print('WLAN verbunden:', wlan.ifconfig())

# I²C initialisieren
i2c = I2C(0, sda=Pin(4), scl=Pin(5))
oled = sh1106.SH1106_I2C(128, 64, i2c)

# OLED-Display initialisieren
oled.fill(0)
oled.show()

# Server einrichten
addr = socket.getaddrinfo('0.0.0.0', 1234)[0][-1]
sock = socket.socket()
sock.bind(addr)
sock.listen(1)

print('Warte auf PC Verbindung...')

def display_message(message):
    oled.fill(0)
    oled.text(message, 0, 0)
    oled.show()

while True:
    conn, addr = sock.accept()
    print('Verbindung von', addr)
    
    while True:
        data = conn.recv(1024)
        if not data:
            break
        
        command = data.decode().strip().upper()
        if command == 'X':
            print('Socket auf PC geschlossen')
            display_message('Socket zuuuu')
            time.sleep(5)
        elif command == 'AN':    
            led.value(1)
            print('LED an')
            display_message('LED an')
        elif command == 'AUS':
            led.value(0)
            print('LED aus')
            display_message('LED aus')
        elif command == 'BLINK':
            for _ in range(5):  # Blinkt 5 Mal
                led.toggle()
                time.sleep(0.5)
            led.value(0)
            print('LED blinkt')
            display_message('LED blinkt')
        else :
            print(command)
            display_message(command)            

    conn.close()
