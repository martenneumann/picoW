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
pin_AckSimulation	= Pin(const.gpio_sumulationsStellwReq, Pin.OUT)

########################################################################################################
# 
########################################################################################################
def sendeSimulierteStellwerksAntwort(flankeRichtung):
    logger.log("************************************************************************", "SIMULATION")
    if flankeRichtung == const.stellwSimulationSteigendeFlanke :
        logger.log("Stellwerk Antwort wird Simuliert : Steigende Flanke an GPIO 0", "SIMULATION")
    if flankeRichtung == const.stellwSimulationFallendeFlanke :
        logger.log("Stellwerk Antwort wird Simuliert : Fallende Flanke an GPIO 0", "SIMULATION")
    logger.log("************************************************************************", "SIMULATION")
    pin_AckSimulation.value(flankeRichtung)
    utime.sleep_ms(10)
    
########################################################################################################
# 
########################################################################################################    
def checkeAckVonSimmulation(flankenRichtung):
    testaturEingabe = simulationsStuff.pruefeAufTestaturEingabe()
    if testaturEingabe == "o":
        sendeSimulierteStellwerksAntwort(flankenRichtung)
   if testaturEingabe == "f":
        sendeSimulierteStellwerksAntwort(flankenRichtung)         
########################################################################################################
# 
########################################################################################################
def anfrageStellenAntwortAbwarten():
     pin_Req.value(1)
     utime.sleep(1) #  Gegen Tasten Prellen
     
     while(pin_Ack.value() != 1):
         checkeAckVonSimmulation(const.stellwSimulationSteigendeFlanke) # Nur zur Simulation notwendig
         utime.sleep_ms(10)
         
     pin_Req.value(0)
     
     while(pin_Ack.value() != 0):
         checkeAckVonSimmulation(const.stellwSimulationFallendeFlanke) # Nur zur Simulation notwendig
         utime.sleep_ms(10)

     return True
    
########################################################################################################
# 
########################################################################################################
def weichenOeffnenErlaubtAnfragenAntwortAbwarten():
    logger.log("WeichenOeffnenAnfragen::Darf Weiche geoeffnet werden? Warte aktiv auf OK!!!", "REQ")
    logger.log("Zur Simulation kann PIN 1 / GPIO 0 mit 5V VCC verbunden werden. Dann wieder ziehen", "REQ") 
    if anfrageStellenAntwortAbwarten():
        logger.log("WeichenOeffnenAnfragen::Weiche oeffnen erlaubt", "ACK")
        return True
    
    
########################################################################################################
# 
########################################################################################################
def weichenSchliessenErlaubtAnfragenAntwortAbwarten():
    logger.log("WeichenSchliessenErlaubtAnfragenAntwortAbwarten::Darf Weiche geschlossen werden? Warte aktiv auf OK!!!", "REQ") 
    if anfrageStellenAntwortAbwarten():
        logger.log("WeichenSchliessenErlaubtAnfragenAntwortAbwarten::Weiche schliessen erlaubt", "ACK")
        return True     
