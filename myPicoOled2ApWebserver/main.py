# Pico Accespoint + Web Server
import network
import socket
from machine import Pin, I2C, reset
import time


#------------------------------------------------------------------------
#config
ssid = "my_pico2"
pwd  = "12345678"
#------------------------------------------------------------------------
print("Hallo")
def test_ap(ap):
    if ap.active():
        print("Access Point ist aktiv.")
        print(f"SSID: {ap.config('essid')}")
        print(f"IP: {ap.ifconfig()[0]}")
        print('pwd : 12345678')
    else:
        print("Access Point ist nicht aktiv.")

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



