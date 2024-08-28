import socket

# Verbindung zum Pico W aufbauen
print("PC WLAN VERBINDER")
pico_ip = '192.168.178.29'  # Ersetze dies durch die IP-Adresse deines Pico W
pico_port = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((pico_ip, pico_port))

def send_command(command):
    sock.sendall(command.encode())
    print(f'Befehl "{command}" gesendet')

while True:
    command = input('Gib "AN", "AUS", oder "BLINK" ein: ').strip().upper()
    if command in ['AN', 'AUS', 'BLINK']:
        send_command(command)
    else:
        print('Ungültiger Befehl!')

# Verbindung schließen (optional)
# sock.close()
