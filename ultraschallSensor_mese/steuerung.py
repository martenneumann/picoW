# Bibliotheken laden
from time import sleep_ms, sleep
import init
import sensoren
import logger
import utime


##############################################################################################################################################
# 
##############################################################################################################################################
sleepTime = 100
anzahlMessungenProSample = 10
dumpForm = 1
messungsKorrekturFaktor = 1
messungs_Array = []
erwartungUndAbweichung_Array = []
START_TIME = utime.ticks_ms()
i = 0

##############################################################################################################################################
##############################################################################################################################################


##############################################################################################################################################
# 
##############################################################################################################################################
def getArithmetischesMittelFromMessungsArray(myMessungs_Array) :
    return sum(myMessungs_Array) / len(myMessungs_Array)

##############################################################################################################################################
# https://www.leifiphysik.de/akustik/schallgeschwindigkeit/grundwissen/einflussfaktoren-auf-die-schallgeschwindigkeit
##############################################################################################################################################
def getSchallgeschwindigkeit(aktuelleTemperatur) :
    return 331.3 + (0.6 * aktuelleTemperatur)

##############################################################################################################################################
# Tonlaufzeit auf die einheit Sekunden umrechnen
# return in Meter
##############################################################################################################################################
def tonlaufzeit2Strecke(tonLaufzeit, aktuelleTemperatur) :
    return (( tonLaufzeit / 1_000_000.0 ) * getSchallgeschwindigkeit(aktuelleTemperatur)) / 2

##############################################################################################################################################
# 
##############################################################################################################################################
def setEntfernungsArray(aktuelleTemperatur) :
    for y in range(anzahlMessungenProSample) :
        tonLaufzeit = sensoren.getTonlaufzeit()
        streckeInMeter = tonlaufzeit2Strecke(tonLaufzeit, aktuelleTemperatur)
        streckeInMeterKorregiert = streckeInMeter * messungsKorrekturFaktor
        messungs_Array.append(streckeInMeter)

##############################################################################################################################################
# 
##############################################################################################################################################
def setMessungsKorrekturFaktor(myMessungsKorrekturFaktor) :
    messungsKorrekturFaktor = myMessungsKorrekturFaktor
    
##############################################################################################################################################
# 
##############################################################################################################################################
def getSpeed(d1, d2, t) :
    return (d2 - d1) / (t/1000)

##############################################################################################################################################
# 
##############################################################################################################################################
def getVarianzFromMessungsArray(aritMittel) :
    varianz_array = []
    for x in messungs_Array : varianz_array.append((x - aritMittel) ** 2)
    return varianz_array

##############################################################################################################################################
# 
##############################################################################################################################################
def getStandartAbweichung(varianzen_Array) :
    return ((1 / (len(varianzen_Array) - 1)) * sum(varianzen_Array)) ** 0.5

    
##############################################################################################################################################
##############################################################################################################################################
def main():
    global i
    global messungs_Array
    
    while True :

        if i % 10 == 0 : aktuelleTemperatur	= sensoren.getTemperatur()    

        messungs_Array	= setEntfernungsArray(aktuelleTemperatur)
        aritMittel 		= getArithmetischesMittelFromMessungsArray(messungs_Array)
        varianzen_Array	= getVarianzFromMessungsArray(aritMittel)
        stdAbweichung 	= getStandartAbweichung(varianzen_Array)
        erwartungUndAbweichung_Array.append([aritMittel, stdAbweichung])
    
        if (i == 0) : speed = 0
        else : speed = getSpeed(erwartungUndAbweichung_Array[-1][0], erwartungUndAbweichung_Array[-2][0], sleepTime)
    
        logger.dump(dumpForm, i, messungs_Array, erwartungUndAbweichung_Array, speed)
    
        sleep(1)
        i += 1
        
        messungs_Array = []


##############################################################################################################################################
##############################################################################################################################################
if __name__ == "__main__":
    print("hallo")
    init.initial()
    main()    
    