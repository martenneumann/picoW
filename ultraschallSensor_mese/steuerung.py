# Bibliotheken laden
from time import sleep_ms, sleep
from utime import sleep_us, ticks_us
import init
import sensoren
import logger
import utime


##############################################################################################################################################
# 
##############################################################################################################################################
sleepTime 						= 2000  # Millisekunden
sleepTimeZwischenMessungen		= 5    # Millisekunden
anzahlMessungenProSample		= 10
dumpCSV 						= 0
dumpHMI							= 1
dumpNurSpeed					= 2
#messungsKorrekturFaktor			= 0
#messungs_Array					= []
#messungs_korrigiert_Array		= []
#erwartungUndAbweichung_Array	= []
#START_TIME						= utime.ticks_ms()
i								= 0

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
# return in cm
##############################################################################################################################################
def tonlaufzeit2Strecke(tonLaufzeit, aktuelleTemperatur) :
    return (( tonLaufzeit / 1_000_000.0 ) * getSchallgeschwindigkeit(aktuelleTemperatur)) / 2

##########################################################################################################################################
# 
##########################################################################################################################################
def calkAndSetNewSleepTime() :
    global sleepTime
    global sleepTimeZwischenMessungen
    global anzahlMessungenProSample
    sleepTime = sleepTime - (sleepTimeZwischenMessungen * anzahlMessungenProSample)
    
##############################################################################################################################################
# 
##############################################################################################################################################
def setEntfernungsArray(aktuelleTemperatur) :
    messungs_Array = []
    messungs_korrigiert_Array = []
    messungsKorrekturFaktor = init.getMessungsKalibrierFaktor()
    for y in range(anzahlMessungenProSample) :
        tonLaufzeit = sensoren.getTonlaufzeit()
        streckeInCm = tonlaufzeit2Strecke(tonLaufzeit, aktuelleTemperatur)
        streckeInCmKorregiert = streckeInCm + messungsKorrekturFaktor
        messungs_Array.append(streckeInCm)
        messungs_korrigiert_Array.append(streckeInCmKorregiert)
        sleep_us(sleepTimeZwischenMessungen)
    return messungs_Array, messungs_korrigiert_Array
    
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
    global sleepTime
    aritMittel_lastLoop = 0
    while True :

        if i % 100 == 0 : aktuelleTemperatur	= sensoren.getTemperatur()
        
        messungs_Array , messungs_korregiert_Array	= setEntfernungsArray(aktuelleTemperatur)
        aritMittel 		= getArithmetischesMittelFromMessungsArray(messungs_korregiert_Array)
        varianzen_Array	= getVarianzFromMessungsArray(aritMittel)
        stdAbweichung 	= getStandartAbweichung(varianzen_Array)
    
        if (i == 0) : speed = 0
        else : speed = getSpeed(aritMittel, aritMittel_lastLoop, sleepTime)
        print(f"aritMittel_lastLoop -> {aritMittel_lastLoop} | aritMittel -> {aritMittel} | speed -> {speed} ")
        aritMittel_lastLoop = aritMittel
    
        #logger.dump(dumpNurSpeed, i, messungs_Array, messungs_korregiert_Array, aritMittel, stdAbweichung, speed, init.getMessungsKalibrierFaktor(), aktuelleTemperatur)
        sleep_ms(sleepTime)
        i += 1
        

##############################################################################################################################################
##############################################################################################################################################
if __name__ == "__main__":
    init.initial()
    calkAndSetNewSleepTime()
    sleep(1)
    main()

    