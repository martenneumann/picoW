# main.py
import logger
import utime
import _thread

from machine import Pin, PWM

########################################################################################################
#    Hier werden die GPIO Pins definiert
########################################################################################################
pin_Ack 			= Pin(0, Pin.IN) 
pin_Req 			= Pin(1, Pin.OUT) 
pin_Lichtschranke 	= Pin(2, Pin.IN)
pin_GleisIn1		= Pin(3, Pin.OUT)
pin_GleisIn2		= Pin(4, Pin.OUT)
pin_GleisPwm		= PWM(Pin(6))

########################################################################################################
#   Globale Variablen
########################################################################################################
stop_flagLichtschranke 	= False
lSchranke_keinZug 		= 1 # objErkannt == 0 obNichtErkannt ==1
weicheAuf				= 1
weicheZu				= 0
gleisEinfahrt			= 1
gleisAusfahrt			= 0
gleisTraegerFrequenz	= 100
gleisDutyProzent		= 100


# Klasse für Sensoren (Ersatz für Enum)
class Sensor:
    LICHTSCHRANKE1 = ("Lichtschranke 1", 1)
    LICHTSCHRANKE2 = ("Lichtschranke 2", 2)
    READKONTAKT = ("Readkontakt", 3)

########################################################################################################
# 
########################################################################################################
def stelleEineAnfrage():
     pin_Req.value(1)
     utime.sleep(1) #  Gegen Tasten Prellen
     while(pin_Ack.value() != 1): utime.sleep(1)
     pin_Req.value(0)
     while(pin_Ack.value() != 0): utime.sleep(1)
     return True

     
    
########################################################################################################
# 
########################################################################################################
def weichenOeffnenAnfragen():
    logger.log("weichenOeffnenAnfragen::Darf Weiche geoeffnet werden?", "REQ")
    if stelleEineAnfrage():
        logger.log("weichenOeffnenAnfragen::Weiche oeffnen erlaubt", "ACK")
        return True


########################################################################################################
# 
######################################################################################################## 
def lichtschranknÜberwachungStarten():
    global stop_flagLichtschranke
    global lSchranke_keinZug
    while not stop_flagLichtschranke:
        if pin_Lichtschranke.value() != lSchranke_keinZug:
            lSchranke_keinZug = pin_Lichtschranke.value()
            logger.log(f"Zustandswechsel Lichtschranke lSchranke_keinZug='{lSchranke_keinZug}'", "L-SCHRANKE")
        utime.sleep(1)
    
########################################################################################################
# 
######################################################################################################## 
def lichtschranknÜberwachungStoppen():
    global stop_flagLichtschranke
    logger.log("Thread zum Lichtschrankenüberwachung gestoppt.", "INFO")
    stop_flagLichtschranke = True
    utime.sleep(1)

    
########################################################################################################
# 
########################################################################################################    
def weicheSteuern(position):
    #TODO
    if lSchranke_keinZug == 0 :
        logger.log("Weiche oeffnen erlaubt aber Zug im Weichenbereich. EXIT -1", "ERR")
        exit -1
        
    if position == weicheAuf :
        logger.log("Weiche oeffnen", "WEICHE")
        
    if position == weicheZu :
        logger.log("Weiche schliessen", "WEICHE")
    
    return True

########################################################################################################
# 
########################################################################################################    
def warteAufZug():
    logger.log("Warten auf Zugeinfahrt in Weichenbereich", "L-SCHRANKE")
    while (lSchranke_keinZug != 0) : utime.sleep(1)
    logger.log("Zug im offenen Weichenbereich erkannt", "L-SCHRANKE")

########################################################################################################
# 
########################################################################################################    
def gleiseUnterStrom(richtung):
    if richtung == gleisEinfahrt:
        logger.log("Setzte gleise für EINFAHRT Unter Strom.", "H_Brücke")
    elif richtung == gleisAusfahrt:
        logger.log("Setzte gleise für AUSFAHRT Unter Strom.", "H_Brücke")
        

    
        
########################################################################################################
#
#    Wandelt einen Prozentwert (0 bis 100%) in einen uint16-Wert (0 bis 65535) um.
#
#    Args:
#        percentage (float): Der Prozentwert (0.0 bis 100.0)
#
#    Returns:
#        int: Der entsprechende uint16-Wert (0 bis 65535).
########################################################################################################            
def prozen2u16(percentage):
    return int((percentage / 100) * 65535)       

########################################################################################################
if __name__ == "__main__":
    #while(True):
        logger.log("Kran Programm gestartet.", "INFO")
        
        # Starte Lichtschranken ueberwachung
        logger.log("Thread zum Lichtschrankenüberwachung gestartet.", "INFO")
        _thread.start_new_thread(lichtschranknÜberwachungStarten, ())
        
        # Warte auf die erlaubniss die Weiche zu öffnen
        if weichenOeffnenAnfragen():
            weicheSteuern(weicheAuf)
        
        
        warteAufZug()
        gleiseUnterStrom(gleisEinfahrt)
        
        

        lichtschranknÜberwachungStoppen()

















