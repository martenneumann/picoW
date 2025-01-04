# main.py
import logger
import stellwAnfrage
import motorenSteuern
import sensorUeberwachung
import utime
import _thread

from machine import Pin, PWM

########################################################################################################
#    Hier werden die GPIO Pins definiert
########################################################################################################
pin_GleisIn1		= Pin(3, Pin.OUT)
pin_GleisIn2		= Pin(4, Pin.OUT)
pin_GleisPwm		= PWM(Pin(6))


########################################################################################################
#   Globale Variablen
########################################################################################################
gleisEinfahrt			= 1
gleisAusfahrt			= 0
gleisTraegerFrequenz	= 100
gleisDutyProzent		= 100



########################################################################################################
# 
########################################################################################################    
def warteAufZug():
    logger.log("Warten auf Zugeinfahrt in Weichenbereich", "L-SCHRANKE")
    while (sensorUeberwachung.lSchranke_ZugErkannt != 1) : utime.sleep(1)
    logger.log("Zug im offenen Weichenbereich erkannt", "L-SCHRANKE")

########################################################################################################
# 
########################################################################################################    
def gleiseUnterStrom(richtung):
    if richtung == gleisEinfahrt:
        logger.log("Setzte gleise für EINFAHRT Unter Strom.", "H_Brücke")
    elif richtung == gleisAusfahrt:
        logger.log("Setzte gleise für AUSFAHRT Unter Strom.", "H_Brücke")
    #TODO    

    
        
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
        _thread.start_new_thread(sensorUeberwachung.sensorUberwachungStarten, ())
        utime.sleep(1) #  Gegen Kernkonflikt
        
        # Warte auf die erlaubniss die Weiche zu öffnen
        stellwAnfrage.weichenOeffnenErlaubtAnfragenAntwortAbwarten()
        motorenSteuern.weicheOeffnen()
        
        
        warteAufZug()
        gleiseUnterStrom(gleisEinfahrt)
        #TODO Bremsen
        

        sensorUeberwachung.sensorUberwachungStoppen()
        utime.sleep(1) #  Damit Kern1 vor Kern0 (main) beendet wird
        logger.log("Kran Programm beendet.", "INFO")
















