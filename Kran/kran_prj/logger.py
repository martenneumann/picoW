#Getestet
import utime

# Initialisiere den Startzeitpunkt
START_TIME = utime.ticks_ms()

########################################################################################################
#    Gibt die Zeit seit dem Start des Programms in Sekunden zurück.
########################################################################################################
def hohleZeitstempel():
    sysZeit = utime.ticks_diff(utime.ticks_ms(), START_TIME) // 1000
    minutes = sysZeit // 60
    seconds = sysZeit % 60
    return f"{minutes:02}:{seconds:02}"

########################################################################################################
#    Loggt eine Nachricht mit einem relativen Zeitstempel und Log-Level.
########################################################################################################
def log(nachricht, komponente="INFO"):
    zeitStempel = hohleZeitstempel()
    print(f"[{zeitStempel}] [{komponente}] {nachricht}")
