# main.py
import logger
import const
import stellwAnfrage
import weichenSteuerung
import sensorUeberwachung
import utime
import ladeZyklen
import zugSteuerung


########################################################################################################
# 
########################################################################################################    
def warteAufZugImWeichenbereich():
    logger.log("Warten auf Zugeinfahrt in Weichenbereich (Lichtschranke Blockiert)", "INFO")
    while (sensorUeberwachung.lSchranke_ZugErkannt != 1) : utime.sleep(1)
    logger.log("Zug im offenen Weichenbereich erkannt", "L-SCHRANKE")
       
########################################################################################################
if __name__ == "__main__":
    while(True):
        # INIT
        logger.log("Kran Programm gestartet.", "INFO")
        weichenSteuerung.weicheInitalSchliessen()
        
        # Starte Sensor ueberwachung
        sensorUeberwachung.sensorUberwachungStarten()
        
        # Warte auf die erlaubniss die Weiche zu öffnen
        stellwAnfrage.weichenOeffnenErlaubtAnfragenAntwortAbwarten()
        weichenSteuerung.weicheOeffnen()
        
        warteAufZugImWeichenbereich()
        utime.sleep(5)
        
        # Erster haltepunkt
        zugSteuerung.fahreZugRein(const.minZugSpeed, const.abbruchsZeitInMs_ZugReinfahren)
        logger.log("Zug hat Haltepunkt erreicht.", "INFO")
        utime.sleep(5)
        
        # Weiche schliessen
        stellwAnfrage.weichenSchliessenErlaubtAnfragenAntwortAbwarten() # Warte auf die erlaubniss die Weiche zu schliessen
        weichenSteuerung.weicheSchliessen()
        utime.sleep(5)        
        
        # Zug end- und beladen
        ladeZyklen.fahreEntladeUndBeladeZyclus()
        utime.sleep(5)
        
        # Warte auf die erlaubniss die Weiche zu öffnen
        stellwAnfrage.weichenOeffnenErlaubtAnfragenAntwortAbwarten()
        weichenSteuerung.weicheOeffnen()
        utime.sleep(5)
        
        zugSteuerung.fahreZugRaus(const.minZugSpeed, const.abbruchsZeitInMs_ZugRausfahren)        
        utime.sleep(5)
        
        # Warte auf die erlaubniss die Weiche zu schliessen        
        stellwAnfrage.weichenScchliessenErlaubtAnfragenAntwortAbwarten() 
        weichenSteuerung.weicheSchliessen() 

    sensorUeberwachung.sensorUberwachungStoppen()
    utime.sleep(1) #  Damit Kern1 vor Kern0 (main) beendet wird
    logger.log("Kran Programm beendet.", "INFO")
















