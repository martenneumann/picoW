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
import sys
import select
import logger

########################################################################################################
# Pruefe durchgaengig ob der Nutzer etwas ueber seine Tastatur (Konsole der Thonny IDE) eingegeben
# hat und mit enter bestaetigt.
# Alle Tasten zählen ausser es wurde nur Enter gedruekt. Dies sendet das System manchmal
# bei Programmstart mit, deshalb schließen wir es aus
#
# 1. Ueberpruef ueber das Betriebssystem (sys) vom Pico die standart input (.stdin)
#    Findet sich hier etwas, gab es eine Tastatureingabe
#    Hier im abschnitt select.select(rlist, wlist, xlist[, timeout]) gut erklärt
#    https://docs.python.org/3/library/select.html
# 2. Ließt aus dem System, ueber die standard Eingabe eine gesamte Zeile, bis zum Enter ein
#    (dh. sollte der Nutzer enter druecken)
# 3. Entfernt das Enter aus dem eingelesenen String, da nicht benötigt (strip())
# 4. Ueberpruefe ob eingabe nicht leer ist. Dies kann passiere, wenn nur Enter gedrueckt wurde
#    dann ist readline() == /n strip() entfernt es aber und dadurch wird eingabe == ""
# 5. Logge
#
# @return : Buchstabenfolge die ueber die Tastatur eingegeben wurde bis zum Enter oder
#           NONE wenn der Nutzer bei Funktionsaufruf nichts eingegeben hat
#
########################################################################################################
def pruefeAufTestaturEingabe():
    if select.select([sys.stdin], [], [], 0)[0]:
        eingabe = sys.stdin.readline().strip()
        if eingabe == "" : return None
        logger.log(f"ACHTUNG : Es gab eine Tastatureingabe : '{eingabe}'", "SIMULATION")
        return eingabe
    return None
