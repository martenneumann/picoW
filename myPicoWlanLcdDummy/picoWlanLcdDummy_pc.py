import socket
print("WLAN PICO VERBINDER")

# Verbindung zum Pico W aufbauen
pico_ip = '192.168.178.29'  # Ersetze dies durch die IP-Adresse deines Pico W
pico_port = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((pico_ip, pico_port))

def send_command(command):
    sock.sendall(command.encode())
    print(f'Befehl "{command}" gesendet')

send_command("Verbunden")

while True:
    command = input('Gib "AN", "AUS" oder "BLINK" ein für LED. Sonst Text: ').strip().upper()
    if command in ['AN', 'AUS', 'BLINK']:
        send_command(command)
    elif command in ['X']:
        # Verbindung schließen
        print("Schließe Socket auf meinem PC")
        send_command(command)
        sock.close()
        exit(0)
    else:
        print('Ungültiger LED Befehl. Printe nur auf Display!')
        send_command(command)

