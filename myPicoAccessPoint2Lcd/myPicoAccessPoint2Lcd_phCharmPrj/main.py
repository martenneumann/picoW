import socket

print("Pico W Access Point Verbindung")

# Verbindung zum Pico W aufbauen
pico_ip = '192.168.4.1'  # Standard-IP-Adresse des Pico W im AP-Modus
pico_port = 1234         # Port, auf dem Pico lauscht

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((pico_ip, pico_port))
    print("Verbunden")
except Exception as e:
    print(f"Fehler bei der Verbindung: {e}")
    exit(1)

def send_command(command):
    sock.sendall(command.encode())
    print(f'Befehl "{command}" gesendet')

while True:
    command = input('Gib "AN", "AUS" oder "BLINK" ein für LED. Gib "CLEAN" fuer OLED ein. Sonst Text: ').strip().upper()
    send_command(command)

    if command in ['X']:
        # Verbindung schließen
        print("Schließe Socket auf meinem PC")
        sock.close()
        exit(0)
