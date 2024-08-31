# Pico Accespoint + Web Server
import network
import socket
from machine import Pin, I2C, reset
import time
import sh1106

#------------------------------------------------------------------------
#config
ssid = "my_pico"
pwd  = "12345678"
sdaPin = 4
sclPin = 5
hoeheZeile = 10
#------------------------------------------------------------------------

i2c = I2C(0, sda=Pin(sdaPin), scl=Pin(sclPin))
oled = sh1106.SH1106_I2C(128, 64, i2c)

oled.fill(0)
oled.show()

led = Pin("LED", Pin.OUT)

def scrolle_hoch(in_px):
    for i in range(in_px):
        oled.scroll(0, -1)
        oled.show()
        time.sleep(0.05)

def display_message(message, zeile=0):
    if zeile == 0:
        oled.fill(0)    
    oled.text(message, 0, (zeile * hoeheZeile))
    if message == 'CLEAN' : oled.fill(0) 
    oled.show()

def my_log(msg, zeile=0):
    display_message(msg, zeile)
    print(msg)
    
my_log("AP + Webserv", 0)    

def tuWas(command):
    if command == "AN":
        led.on()
    elif command == "AUS":
        led.off()
    elif command == "BLINK":
        for _ in range(5):
            led.on()
            time.sleep(0.5)
            led.off()
            time.sleep(0.5)
    elif command == "CLOSE":
        #cl.close()
        #time.sleep(2)
        my_log("Reset von serv", 0)
        #reset()

def test_ap(ap):
    if ap.active():
        my_log("Access Point ist aktiv.", 1)
        my_log(f"SSID: {ap.config('essid')}", 2)
        my_log(f"IP: {ap.ifconfig()[0]}", 3)
        my_log('pwd : 12345678', 4)
    else:
        my_log("Access Point ist nicht aktiv.", 1)

def setup_ap():
    ap = network.WLAN(network.AP_IF)
    ap.active(False)
    time.sleep(2)
    ap.active(True)
    ap.config(essid=ssid, password=pwd, channel=6)
    ap.active(True)
    test_ap(ap)
    return ap.ifconfig()[0]

def start_webserver(ip):
    addr = socket.getaddrinfo(ip, 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print('Webserver gestartet auf http://{}'.format(ip))
    display_message("Webserver run!", 5)
    
    while True:
        cl, client_addr = s.accept()
        print("--------------------------------------------------")
        print('Client verbunden von', client_addr)
        display_message(str(client_addr), 5)
        request = cl.recv(1024).decode('utf-8')
        
        if 'GET /?message=' in request:
            try:
                message = request.split('GET /?message=')[1].split(' ')[0]
                message = message.replace('+', ' ')
                display_message(message, 0)
                print(message)
            except IndexError:
                pass
            
        if 'GET /?command=' in request:
            try:
                command = request.split('GET /?command=')[1].split(' ')[0]
                tuWas(command.upper())
                print(command.upper())
            except IndexError:
                pass            
        
        # HTML-Seite zurückgeben
        html = """<!DOCTYPE html>
<html>
    <head>
        <title>OLED und LED Steuerung</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 10px;
            }
            h1 {
                font-size: 24px;
            }
            form {
                margin-bottom: 20px;
            }
            input[type="text"] {
                width: 80%;
                padding: 10px;
                font-size: 18px;
            }
            input[type="submit"], button {
                padding: 10px 20px;
                font-size: 18px;
                margin-top: 10px;
                margin-bottom: 10px;
            }
            button {
                width: 45%;
                margin: 5px;
            }
        </style>
    </head>
    <body>
        <h1>Nachricht eingeben</h1>
        <form action="/" method="get">
            <input type="text" name="message" placeholder="Nachricht eingeben" />
            <input type="submit" value="Senden" />
        </form>
        
        <h1>LED Steuerung</h1>
        <p>
            <a href="/?command=AN"><button>LED Ein</button></a><br>
            <a href="/?command=AUS"><button>LED Aus</button></a><br>
            <a href="/?command=BLINK"><button>LED Blinken</button></a><br>
        </p>
        <h1>Steuerung Pico</h1>
        <p>
            <a href="/?command=CLOSE"><button>Close</button></a>
        </p>        
    </body>
</html>"""
        
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(html)
        cl.close()

ip = setup_ap()
start_webserver(ip)



