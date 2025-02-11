# Bibliotheken laden
from time import sleep_ms


##############################################################################################################################################
# 
##############################################################################################################################################
sleepTime = 100
counter   = 0
messwerteStehendesObjekt

##############################################################################################################################################
# https://www.leifiphysik.de/akustik/schallgeschwindigkeit/grundwissen/einflussfaktoren-auf-die-schallgeschwindigkeit
##############################################################################################################################################
def getSchallgeschwindigkeit(aktuelleTemperatur) :
    return 331.3 + (0.6 * aktuelleTemperatur)
##############################################################################################################################################
# Tonlaufzeit auf die einheit Sekunden umrechnen
# return in Meter
##############################################################################################################################################	
def tonlaufzeit2Strecke(tonLaufzeit) :
    return (( tonLaufzeit / 1_000_000.0 ) * getSchallgeschwindigkeit()) / 2


##############################################################################################################################################
##############################################################################################################################################
# Wiederholung (Endlos-Schleife)
while True :
    
    if counter % 10 == 0 :
        aktuelleTemperatur	= getTemperatur()    

    for i in range(10) :
        tonLaufzeit 	= getTonlaufzeit()
        streckeInMeter	= tonlaufzeit2Strecke(tonLaufzeit, aktuelleTemperatur)
        messwerteStehendesObjekt.append(streckeInMeter)
    

    

    sleep(sleepTime)
    couter += sleepTime