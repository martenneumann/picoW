import logger
import const
import utime
import _thread
from machine import Pin

########################################################################################################
#    Hier werden die GPIO Pins definiert
########################################################################################################
pin_Lichtschranke	= Pin(const.gpio_LichtschrankeLesen, Pin.IN)
pin_ReedSchalter	= Pin(const.gpio_ReetSchalterLesen, Pin.IN, Pin.PULL_DOWN)

########################################################################################################
#   Globale Variablen
########################################################################################################
stop_flagThread1	 	= False
lSchranke_ZugErkannt 	= 0 # objErkannt == 1 obNichtErkannt == 0
reedSchalter_ZugErkannt	= 0 # objErkannt == 1 obNichtErkannt == 0

########################################################################################################
# Reed
######################################################################################################## 
def sensorUberwachungStarten():
    _thread.start_new_thread(sensorUberwachungsLoop, ())  
    utime.sleep(1) #Gegen Kernkonflikt
        
########################################################################################################
# Reed
######################################################################################################## 
def sensorUberwachungsLoop():        
    global stop_flagThread1
    logger.log("Sensor ueberwachungs Thread geastartent", "INFO")
    while not stop_flagThread1:
        lichtschrankeUeberwachen()
        reedSchalterUeberwachen()
        utime.sleep_ms(50)    
        
########################################################################################################
# 
######################################################################################################## 
def sensorUberwachungStoppen():
    global stop_flagThread1
    logger.log("Sensor ueberwachungs Thread gestoppt", "INFO")
    stop_flagThread1 = True
    utime.sleep(1)        
        
########################################################################################################
#
######################################################################################################## 
def lichtschrankeUeberwachen():
    global lSchranke_ZugErkannt
    if pin_Lichtschranke.value() != lSchranke_ZugErkannt :
        logger.log(f"Zustandswechsel Lichtschranke lSchranke_ZugErkannt='{lSchranke_ZugErkannt}'", "L-SCHRANKE")
    if pin_Lichtschranke.value() ==  0 : lSchranke_ZugErkannt = 0
    else :  lSchranke_ZugErkannt = 1

        
########################################################################################################
# Reed
######################################################################################################## 
def reedSchalterUeberwachen():
    global reedSchalter_ZugErkannt
    reed_state = pin_ReedSchalter.value()
    if reed_state != reedSchalter_ZugErkannt :
        if reed_state == 0 : reedSchalter_ZugErkannt = 0
        else : reedSchalter_ZugErkannt = 1
        logger.log(f"Zustandswechsel Reed Schalter reedSchalter_ZugErkannt='{reedSchalter_ZugErkannt}'", "Reeed")
