# @name AccessPoint + PC Programm
# @date 2024-08-31

import network
import socket
from machine import Pin, I2C, reset
import time
import sh1106  # Stelle sicher, dass diese Bibliothek vorhanden ist

#-----------------------------------------------------------------------------------
# CONF
ssid = "my_pico"  # SSID für den Access Point
pwd  = "12345678"  # Passwort für den Access Point

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

# Scrollen nach oben ---> Geht noch nicht
def scrolle_hoch(in_px) :
    for i in range(in_px):
        oled.scroll(0, -1)  # Um 1 Pixel nach oben scrollen
        oled.show()  # Aktualisieren
        oled.sleep(0.05)

# Hiermit Botschaften auf OLED schreiben
def display_message(message, zeile=0):
    if zeile == 0:
        oled.fill(0)    
    oled.text(message, 0, (zeile * hoeheZeile))
    if message == 'CLEAN' : oled.fill(0) 
    oled.show()


# Log meldung in console und OLED
def my_log(msg, zeile=0):
    display_message(msg, zeile)
    print(msg)

# Funktion zum Testen des Access Points
def test_ap(ap):
    if ap.active():
        my_log("Access Point ist aktiv.", 1)
        my_log(f"SSID: {ap.config('essid')}", 2)
        my_log(f"IP: {ap.ifconfig()[0]}", 3)
        my_log('pwd : 12345678', 4)
    else:
        my_log("Access Point ist nicht aktiv.", 1)

# WLAN zurücksetzen und Access Point aktivieren
def setup_ap():
    ap = network.WLAN(network.AP_IF)
    
    # WLAN zurücksetzen (aus und wieder einschalten)
    ap.active(False)
    time.sleep(2)
    ap.active(True)
    
    # Access Point konfigurieren
    ap.config(essid=ssid, password=pwd, channel=6)  # Kanal explizit setzen
    ap.active(True)
    
    # Status testen
    test_ap(ap)
    
    return ap

# Hauptprogramm
my_log("AP + Pc APP", 0)
ap = setup_ap()


# Server einrichten
addr = socket.getaddrinfo('0.0.0.0', 1234)[0][-1]
sock = socket.socket()
sock.bind(addr)
sock.listen(1)

my_log("Warte auf PC ...", 5)

while True:
    try:
        conn, addr = sock.accept()
        my_log("PC verbunden ...", 0)
        
        while True:
            data = conn.recv(1024)
            if not data:
                break

            command = data.decode().strip()
            
            # Überprüfe, ob das Kommando eine Zeile angibt (z.B. "abc/1")
            if '/' in command:
                message, line = command.split('/', 1)
                try:
                    line = int(line)  # Versuche, den Zeilenwert in eine Zahl umzuwandeln
                except ValueError:
                    line = 0  # Falls dies fehlschlägt, setze die Zeile auf 0
            else:
                message = command
                line = 0
            
            
            # Verarbeite spezielle Kommandos
            if message == 'X':
                my_log('Socket zuuuu')
            elif message == 'REBOOT':
                my_log('Rebooting...')
                conn.close()
                sock.close()
                reset()                
                
            elif message == 'AN':
                led.value(1)
                print('LED an')
                display_message('LED an')
            elif message == 'AUS':
                led.value(0)
                print('LED aus')
                display_message('LED aus')
            elif message == 'BLINK':
                print('LED blinkt')
                display_message('LED blinkt')
                for _ in range(5):  # Blinkt 5 Mal
                    led.toggle()
                    time.sleep(0.5)
                led.value(0)
            else:
                print(message)
                display_message(message, line)

        conn.close()

    except Exception as e:
        my_log(f'Fehler: {str(e)}')

