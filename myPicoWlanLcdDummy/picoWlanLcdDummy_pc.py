import socket
print("WLAN PICO VERBINDER")

# Verbindung zum Pico W aufbauen
pico_ip = '192.168.178.29'  # Pico W ip auf FritzBox abgelesen
pico_port = 1234            # Port auf dem Pico lauscht

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((pico_ip, pico_port))

def send_command(command):
    sock.sendall(command.encode())
    print(f'Befehl "{command}" gesendet')

while True:
    command = input('Gib "AN", "AUS" oder "BLINK" ein für LED. Sonst Text: ').strip().upper()
    send_command(command)

    if command in ['X']:
        # Verbindung schließen
        print("Schließe Socket auf meinem PC")
        sock.close()
        exit(0)

