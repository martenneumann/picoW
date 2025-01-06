# main.py
import logger
import const
import stellwAnfrage
import weichenSteuerung
import sensorUeberwachung
import utime
import kranMotoren
import ladeZyklen


########################################################################################################
# 
########################################################################################################    
def warteAufZugImWeichenbereich():
    logger.log("Warten auf Zugeinfahrt in Weichenbereich (Lichtschranke Blockiert)", "INFO")
    while (sensorUeberwachung.lSchranke_ZugErkannt != 1) : utime.sleep(1)
    logger.log("Zug im offenen Weichenbereich erkannt", "L-SCHRANKE")

########################################################################################################
# 
########################################################################################################    
def gleiseUnterStrom(richtung):
    if richtung == const.gleisstromZugRein:
        logger.log("Setzte gleise für EINFAHRT Unter Strom.", "H_Brücke")
    elif richtung == const.gelisstromZugRaus:
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
        
        # Erster haltepunkt
        fahreZugRein(const.minZugSpeed, const.abbruchzeitZugErsterHaltepunkt)
        logger.log("Zug hat ersten Entladepunkt erreicht.", "INFO")
        utime.sleep(5)
        stellwAnfrage.weichenScchliessenErlaubtAnfragenAntwortAbwarten() # Warte auf die erlaubniss die Weiche zu schliessen
        weichenSteuerung.weicheSchliessen()        
        ladeZyklen.fahreEntladeZyclus()
        utime.sleep(5)
        
        #Zweiter haltepunkt
        fahreZugRein(const.minZugSpeed, const.abbruchzeitZugZweiterHaltepunkt)
        logger.log("Zug hat zweiten Entladepunkt erreicht.", "INFO")
        utime.sleep(5)
        ladeZyklen.fahreEntladeZyclus()
        utime.sleep(5)
        
        # Warte auf die erlaubniss die Weiche zu öffnen
        stellwAnfrage.weichenOeffnenErlaubtAnfragenAntwortAbwarten()
        weichenSteuerung.weicheOeffnen()        
        fahreZugRaus(const.minZugSpeed, const.abbruchzeitZugVerlaesstBereich)        
        
        # Warte auf die erlaubniss die Weiche zu schliessen        
        stellwAnfrage.weichenScchliessenErlaubtAnfragenAntwortAbwarten() 
        weichenSteuerung.weicheSchliessen() 

        sensorUeberwachung.sensorUberwachungStoppen()
        utime.sleep(1) #  Damit Kern1 vor Kern0 (main) beendet wird
        logger.log("Kran Programm beendet.", "INFO")
















