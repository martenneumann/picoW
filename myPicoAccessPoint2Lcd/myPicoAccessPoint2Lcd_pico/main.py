import network
import socket
from machine import Pin, I2C
import time
import sh1106  # Stelle sicher, dass diese Bibliothek vorhanden ist

#-----------------------------------------------------------------------------------
# CONF
ssid = "Pico_W_Hotspot"  # SSID für den Access Point
password = "12345678"  # Passwort für den Access Point

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

# Onboard LED
led = Pin("LED", Pin.OUT)

# Hiermit Botschaften auf OLED schreiben
def display_message(message, zeile=0):
    if zeile == 0:
        oled.fill(0)
    oled.text(message, 0, (zeile * hoeheZeile))
    oled.show()
    
# Log meldung in console und OLED
def my_log(msg, wait=0, zeile=0):
    display_message(msg, zeile)
    print(msg)
    time(wait)

#display_message('Starte AP...')
#time.sleep(3)
my_log("Starte AP ...", 3, 0)

# Access Point einrichten
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

#print('Access Point aktiv')
#display_message('AP aktiv', 1)
my_log("AP Aktiv ...", 3, 1)

#print('SSID:', ssid)
#print('IP-Adresse:', ap.ifconfig()[0])
#display_message(f'IP: {ap.ifconfig()[0]}', 2)
my_log(f'IP: {ap.ifconfig()[0]}', 3, 2)

# Server einrichten
addr = socket.getaddrinfo('0.0.0.0', 1234)[0][-1]
sock = socket.socket()
sock.bind(addr)
sock.listen(1)

#print('Warte auf PC Verbindung...')
#display_message('Warte auf PC ...', 3)
my_log("Warte auf PC ...", 3, 3)

while True:
    conn, addr = sock.accept()
    #print('Verbindung von', addr)
    #display_message('PC verbunden', 4)
    my_log("PC verbunden ...", 0, 4)
    
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
            
        else:
            print(command)
            display_message(command)            

    conn.close()
