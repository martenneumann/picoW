########################################################################################################
# Dieses Modul ist ein Hilfsmodul und hat seinerseits kein Interface zu einem Aktor oder Sensor.
# Es hat die aufgabe auf das Thonny Terminal zu loggen um den Benutzer ueber den aktuellen Status
# des Kranprogramms zu informieren. Dies ist für das Debugging unerlaesslich.
#
# Gelogged wird in dem Format :
# [Zeit seit beginn des Karanprogramms] [Modul welches gerade logged zb "H-BRUCKE"] [Prosa Text]
#
# @Status : Getestet Funktioniert
#
########################################################################################################
import utime

# Initialisiere den Startzeitpunkt, nehme einen Zeitstempel
START_TIME = utime.ticks_ms()

########################################################################################################
# Erzeuge Zeitstring fuer die logausgabe
# 1. Hole die Zeitdifferenz zwischen dem aktuellen Zeitpunkt und dem Startzeitpunkt
# 2. Teile durch 1000 um von ms auf sekunden zu kommen
# 3. Teile die absoluten Programmlaufzeit durch 60 aber ohne Rest (wie in der Grundschule)
#    so erhält man nur die vollen beendeten Minuten
# 4. Modulo Operator (diesmal schauen wir uns nur den Rest an) alles von der absoluten
#    Programmlaufzeit was noch von "durch 60" als rest überbleibt muss die verbleibende
#    Sekundenzeit sein (Wie in der Grundschule, Teilen mit Rest; hier interessiert aber
#    nur der Rest)
#
# @return : Gibt die Zeit seit dem Start des Programms als string zurück.
#			 Format [minute seit Programmstart]:[sekunden seit Programmstart]
########################################################################################################
def hohleZeitstempel():
    sysZeit = utime.ticks_diff(utime.ticks_ms(), START_TIME) // 1000
    minutes = sysZeit // 60
    seconds = sysZeit % 60
    return f"{minutes:02}:{seconds:02}"

########################################################################################################
# Loggt eine Nachricht mit einem relativen Zeitstempel zum Programmstart,
# einem Modulnamen und einer Nachricht auf dem Terminal der Thonny IDE
#
# ACHTUNG : Geht natürlich nur wenn print nicht umgeleitet wird
#
# @input : nachricht = freier prosa text als string
# @input : komponente = Name der Komponente die gerade logged als string
#
########################################################################################################
def log(nachricht, komponente="INFO"):
    zeitStempel = hohleZeitstempel()
    print(f"[{zeitStempel}] [{komponente}] {nachricht}")
