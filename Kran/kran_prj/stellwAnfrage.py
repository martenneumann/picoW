import utime
import logger
from machine import Pin

########################################################################################################
#    Hier werden die GPIO Pins definiert
########################################################################################################
pin_Ack 			= Pin(0, Pin.IN) 
pin_Req 			= Pin(1, Pin.OUT)

########################################################################################################
# 
########################################################################################################
def anfrageStellenAntwortAbwarten():
     pin_Req.value(1)
     utime.sleep(1) #  Gegen Tasten Prellen
     while(pin_Ack.value() != 1): utime.sleep(1)
     pin_Req.value(0)
     while(pin_Ack.value() != 0): utime.sleep(1)
     return True
    
########################################################################################################
# 
########################################################################################################
def weichenOeffnenErlaubtAnfragenAntwortAbwarten():
    logger.log("weichenOeffnenAnfragen::Darf Weiche geoeffnet werden? Warte aktiv auf OK!!!", "REQ") 
    if anfrageStellenAntwortAbwarten():
        logger.log("weichenOeffnenAnfragen::Weiche oeffnen erlaubt", "ACK")
        return True
    
########################################################################################################
# 
########################################################################################################
def weichenSchliessenErlaubtAnfragenAntwortAbwarten():
    logger.log("weichenSchliessenErlaubtAnfragenAntwortAbwarten::Darf Weiche geschlossen werden? Warte aktiv auf OK!!!", "REQ") 
    if anfrageStellenAntwortAbwarten():
        logger.log("weichenSchliessenErlaubtAnfragenAntwortAbwarten::Weiche schliessen erlaubt", "ACK")
        return True     