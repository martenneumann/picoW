import logger
import utime
import sensorUeberwachung
from machine import Pin

########################################################################################################
#   Globale Variablen
########################################################################################################
weicheAuf				= 1
weicheZu				= 0

########################################################################################################
# 
########################################################################################################    
def weicheOeffnen():
    logger.log("Weiche oeffnen", "WEICHE")
    weicheSteuern(weicheAuf)
    
########################################################################################################
# 
########################################################################################################    
def weicheSchliessen():
    logger.log("Weiche schliessen", "WEICHE")
    weicheSteuern(weicheZu)
    
########################################################################################################
# 
########################################################################################################    
def weicheSteuern(position):
    #TODO
    if sensorUeberwachung.lSchranke_ZugErkannt == 1 :
        logger.log("Weiche oeffnen erlaubt aber Zug im Weichenbereich. EXIT -1", "ERR")
        sensorUberwachungStoppen()
        exit -1
        
    if position == weicheAuf :
        logger.log("Weiche oeffnen", "WEICHE")
        
    if position == weicheZu :
        logger.log("Weiche schließen", "WEICHE")
    
    return True