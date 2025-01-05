# main.py
import logger
import const
import stellwAnfrage
import weichenSteuerung
import sensorUeberwachung
import utime
import kranMotoren


########################################################################################################
# 
########################################################################################################    
def warteAufZugImWeichenbereich():
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
if __name__ == "__main__":
    #while(True):
        # INIT
        logger.log("Kran Programm gestartet.", "INFO")
        weichenSteuerung.weicheInitalSchliessen()
        
        # Starte Sensor ueberwachung
        sensorUeberwachung.sensorUberwachungStarten()
        
        # Warte auf die erlaubniss die Weiche zu öffnen
        stellwAnfrage.weichenOeffnenErlaubtAnfragenAntwortAbwarten()
        weichenSteuerung.weicheOeffnen()
        
        warteAufZugImWeichenbereich()
        gleiseUnterStrom(const.gleisEinfahrt)
        #TODO Bremsen
        
        kranMotoren.fahreHarkenRunter()
        
        # Warte auf die erlaubniss die Weiche zu schliessen
        stellwAnfrage.weichenSchliessenErlaubtAnfragenAntwortAbwarten()
        weichenSteuerung.weicheSchliessen()

        sensorUeberwachung.sensorUberwachungStoppen()
        utime.sleep(1) #  Damit Kern1 vor Kern0 (main) beendet wird
        logger.log("Kran Programm beendet.", "INFO")
















