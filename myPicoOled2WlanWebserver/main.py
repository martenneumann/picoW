import network
import socket
from machine import Pin, I2C
import time
import sh1106

# WLAN-Verbindung herstellen
ssid = "my2,4GHz"  # Ersetze dies durch die SSID des 2,4 GHz Netzwerks
pwd = "05226091438051783374"  # Ersetze dies durch das WLAN-Passwort

# OLED-Display-Konfiguration
sdaPin = 4
sclPin = 5
hoeheZeile = 10

# I²C initialisieren
i2c = I2C(0, sda=Pin(sdaPin), scl=Pin(sclPin))
oled = sh1106.SH1106_I2C(128, 64, i2c)

# OLED-Display initialisieren
oled.fill(0)
oled.show()

# Funktion zum Anzeigen einer Nachricht auf dem OLED
def display_message(message, zeile=0):
    if zeile == 0:
        oled.fill(0)
    oled.text(message, 0, (zeile * hoeheZeile))
    oled.show()

# Funktion zur WLAN-Verbindung
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, pwd)

    print('Verbindung zu WLAN wird hergestellt...')
    while not wlan.isconnected():
        time.sleep(1)
    print('Verbunden mit WLAN:', wlan.ifconfig())
    return wlan.ifconfig()[0]  # Rückgabe der IP-Adresse

# Funktion zum Starten des Webservers
def start_webserver(ip):
    addr = socket.getaddrinfo(ip, 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print('Webserver gestartet auf http://{}'.format(ip))

    while True:
        cl, addr = s.accept()
        print('Client verbunden von', addr)
        request = cl.recv(1024).decode('utf-8')
        
        # Extrahiere Nachricht aus dem HTTP-Request
        if 'GET /?message=' in request:
            try:
                message = request.split('GET /?message=')[1].split(' ')[0]
                message = message.replace('+', ' ')  # Ersetze URL-encoded spaces
                display_message(message)
            except IndexError:
                pass
        
        # HTML-Seite zurückgeben
        html = """<!DOCTYPE html>
<html>
    <head><title>OLED Webserver</title></head>
    <body>
        <h1>Nachricht eingeben</h1>
        <form action="/" method="get">
            <input type="text" name="message" />
            <input type="submit" value="Senden" />
        </form>
    </body>
</html>"""
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(html)
        cl.close()

# WLAN verbinden und Webserver starten
ip = connect_to_wifi()
start_webserver(ip)
