#GETESTET - FUNKTIONIERT
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
# 
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
# 
########################################################################################################    
def checkeAckVonSimmulation():
    testaturEingabe = simulationsStuff.pruefeAufTestaturEingabe()
    if testaturEingabe == "s" or testaturEingabe == "f" : sendeSimulierteStellwerksAntwort(testaturEingabe)
  
    
########################################################################################################
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
# 
########################################################################################################
def weichenOeffnenErlaubtAnfragenAntwortAbwarten():
    logger.log("Darf Weiche geoeffnet werden? Warte aktiv auf OK!!!", "REQ")
    if anfrageStellenAntwortAbwarten():
        logger.log("Weiche oeffnen erlaubt", "ACK")
        pin_AckSimulation.value(0)
        return True
    
    
########################################################################################################
# 
########################################################################################################
def weichenSchliessenErlaubtAnfragenAntwortAbwarten():
    logger.log("Darf Weiche geschlossen werden? Warte aktiv auf OK!!!", "REQ") 
    if anfrageStellenAntwortAbwarten():
        logger.log("Weiche schliessen erlaubt", "ACK")
        pin_AckSimulation.value(0)
        return True     
