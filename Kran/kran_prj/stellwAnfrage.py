import utime
import const
import logger
from machine import Pin

########################################################################################################
#    Hier werden die GPIO Pins definiert
########################################################################################################
pin_Ack = Pin(const.gpio_stellwAck, Pin.IN) 
pin_Req = Pin(const.gpio_stellwReq, Pin.OUT)

########################################################################################################
# 
########################################################################################################
def anfrageStellenAntwortAbwarten():
     pin_Req.value(1)
     utime.sleep(1) #  Gegen Tasten Prellen
     while(pin_Ack.value() != 1): utime.sleep_ms(10)
     pin_Req.value(0)
     while(pin_Ack.value() != 0): utime.sleep_ms(10)
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