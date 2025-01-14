########################################################################################################
# Stelle Anfrage an das Stellwerk ob die Weiche gestellt werden darf
#
# @Status : Getestet Funktioniert
#
########################################################################################################

########################################################################################################
# Importiere von Module
########################################################################################################
import utime
import const
import logger
import simulationsStuff
from machine import Pin

########################################################################################################
#    Hier werden die GPIO Pins definiert
########################################################################################################
pin_Ack 			= Pin(const.gpio_stellwAck, Pin.IN) 
pin_Req 			= Pin(const.gpio_stellwReq, Pin.OUT)
pin_AckSimulation	= Pin(const.gpio_simulationsStellwReq, Pin.OUT)
pin_AckSimulation.value(0)

########################################################################################################
# Simuliere die Antwort des Stellwerkes
#
# ACHTUNG : Hierzu muss GPIO 2 mit GPIO 0 verbunden werden
#
# @input : String der vom Nutzer ueber Thonny Konssole eingegeben wurde
#
# Wenn der User "s" drueckt wird am GPIO  2 eine steigende Flanke ausgeloest
# Wenn der USer "f" drueckt wird am GPPIO 2 eine fallende Flanke ausgeloesst
########################################################################################################
def sendeSimulierteStellwerksAntwort(testaturEingabe):
    logger.log("************************************************************************", "SIMULATION")
    if testaturEingabe == const.stellwSimulationTasteSteigendeFlanke :
        logger.log("Stellwerk Antwort wird Simuliert : Steigende Flanke an GPIO 0", "SIMULATION")
        pin_AckSimulation.value(1)
    elif testaturEingabe == const.stellwSimulationTasteFallendeFlanke :
        logger.log("Stellwerk Antwort wird Simuliert : Fallende Flanke an GPIO 0", "SIMULATION")
        pin_AckSimulation.value(0)
    else : logger.log("fStellwerk Antwort wird Simuliert : Befehl {testaturEingabe} nicht bekannt", "SIMULATION")     
    logger.log("************************************************************************", "SIMULATION")
    utime.sleep_ms(1)
    
########################################################################################################
# Checke ob es eine Eingabe von Nutzer gab und ob sie "s" oder "f" entspreicht
#
# TODO: Funktion ausbauen, bringt ja nicht wirklich was, kann ohne Probleme in
#       sendeSimulierteStellwerksAntwort() erfolgen
#
########################################################################################################    
def checkeAckVonSimmulation():
    testaturEingabe = simulationsStuff.pruefeAufTestaturEingabe()
    if testaturEingabe == "s" or testaturEingabe == "f" : sendeSimulierteStellwerksAntwort(testaturEingabe)
  
    
########################################################################################################
# Stelle eine Anfrage an das Stellwerk.
#
# In der Dokumentation gibt es zwei Bilder die den Anfragenaustausch genau beschreiben
# Hier sei nur der Code erklaert
#
# 1. Anfragen Pin steigende Flanke
# 2. Warte auf steigende Flanke am Antwort Pin (von Stellwerk oder Simulation)
# 3. Anfragen Pin sinkende Flanke
# 4. Warte auf fallende Flanke am Antwort Pin (von Stellwerk oder Simulation)
#
########################################################################################################
def anfrageStellenAntwortAbwarten():
    pin_Req.value(1)
    utime.sleep(1) #  Gegen Tasten Prellen
     
    while(pin_Ack.value() == 0):
        checkeAckVonSimmulation() # Nur zur Simulation notwendig
        utime.sleep_ms(20)
     
    logger.log("Empfange steigende Flanke vom Stellwerk", "ACK")
    pin_Req.value(0)
     
    while(pin_Ack.value() == 1):
        checkeAckVonSimmulation() # Nur zur Simulation notwendig
        utime.sleep_ms(200)
         
    logger.log("Empfange fallende Flanke vom Stellwerk", "ACK")
    return True
    
########################################################################################################
# Stelle die Anfrage eine Weiche zu oeffnen.
#
# Funktion eig. nur zum genaueren Loggen da
# Simulationspin wird hier noch mal auf 0 gesetzt sollte sich der Pico davor
# durch unvollstaendige Nuttzereingabe aufgehangen haben
#
# @return True = Darf geoeffnet werden; Ein anderer Zustand ist ausgeschlossen
#
########################################################################################################
def weichenOeffnenErlaubtAnfragenAntwortAbwarten():
    logger.log("Darf Weiche geoeffnet werden? Warte aktiv auf OK!!!", "REQ")
    if anfrageStellenAntwortAbwarten():
        logger.log("Weiche oeffnen erlaubt", "ACK")
        pin_AckSimulation.value(0)
        return True
    
    
########################################################################################################
# Stelle die Anfrage eine Weiche zu schliessen.
#
# Funktion eig. nur zum genaueren Loggen da
# Simulationspin wird hier noch mal auf 0 gesetzt sollte sich der Pico davor
# durch unvollstaendige Nuttzereingabe aufgehangen haben
#
# @return True = Darf geschlossen werden; Ein anderer Zustand ist ausgeschlossen
#
########################################################################################################
def weichenSchliessenErlaubtAnfragenAntwortAbwarten():
    logger.log("Darf Weiche geschlossen werden? Warte aktiv auf OK!!!", "REQ") 
    if anfrageStellenAntwortAbwarten():
        logger.log("Weiche schliessen erlaubt", "ACK")
        pin_AckSimulation.value(0)
        return True     
