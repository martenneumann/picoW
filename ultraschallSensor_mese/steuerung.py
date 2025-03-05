# Bibliotheken laden
from time import sleep_ms, sleep
from utime import sleep_us, ticks_us
import _thread
import init
import sensoren
import logger

##############################################################################################################################################
messungNachXms						= 10   # Millisekunden
temperaturNachXmessungenErneuern	= 10
anzahlMessungenProSample			= 10
i									= 0

##############################################################################################################################################
# 
##############################################################################################################################################
def getArithmetischesMittelFromArray(myArray) :
    return sum(myArray) / len(myArray)

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
#def calkAndSetNewSleepTime() :
#    global sleepTime
#    global sleepTimeZwischenMessungen
#    global anzahlMessungenProSample
#    sleepTime = sleepTime - (sleepTimeZwischenMessungen * anzahlMessungenProSample)
    
##############################################################################################################################################
# 
##############################################################################################################################################
def getEntfernungsArray(aktuelleTemperatur) :
    messungs_Array = []
    messungs_korrigiert_Array = []
    messungsKorrekturFaktor = init.getMessungsKalibrierFaktor()
    for y in range(anzahlMessungenProSample) :
        tonLaufzeit = sensoren.getTonlaufzeit()
        streckeInCm = tonlaufzeit2Strecke(tonLaufzeit, aktuelleTemperatur)
        streckeInCmKorregiert = streckeInCm + messungsKorrekturFaktor
        messungs_Array.append(streckeInCmKorregiert)
        sleep_ms(messungNachXms)
    return messungs_Array
    
##############################################################################################################################################
# 
##############################################################################################################################################
def getSpeed(d1, d2, t) :
    return (d2 - d1) / (t/1000)

##############################################################################################################################################
# 
##############################################################################################################################################
def getVarianzFromArray(myArray, aritMittel) :
    varianz_array = []
    for x in myArray :
        varianz_array.append((x - aritMittel) ** 2)
    return varianz_array

##############################################################################################################################################
# 
##############################################################################################################################################
def getStandartAbweichungFromArray(varianzen_Array) :
    return ((1 / (len(varianzen_Array) - 1)) * sum(varianzen_Array)) ** 0.5

##############################################################################################################################################
# 
##############################################################################################################################################
def getSpeedArray(messungs_Array, t):
    speed_Array = []
    #speed_Array.append(0)
    for i in range(len(messungs_Array) - 1):
        speed = getSpeed(messungs_Array[i], messungs_Array[i + 1], t)
        speed_Array.append(speed)
    return speed_Array

##############################################################################################################################################
# 
##############################################################################################################################################
def getStandartAbweichungDesMittelwerts(stdAbweichung) :
    return stdAbweichung / (anzahlMessungenProSample ** 0.5)

##############################################################################################################################################
# 
##############################################################################################################################################
def get2SigmaFromStdAbweichung(myStdAbweichung) :
    return myStdAbweichung * 2

##############################################################################################################################################
##############################################################################################################################################
def main():
    global i, messungs_Array, sleepTime
    while True :

        if i % temperaturNachXmessungenErneuern == 0 : aktuelleTemperatur = sensoren.getTemperatur()
        
        # Entfernungen
        entfernungen_Array							= getEntfernungsArray(aktuelleTemperatur)
        entfenungen_aritMittel						= getArithmetischesMittelFromArray(entfernungen_Array)
        entfernungen_varianzenArray					= getVarianzFromArray(entfernungen_Array, entfenungen_aritMittel)
        entfernungen_stdAbweichung					= getStandartAbweichungFromArray(entfernungen_varianzenArray)
        entfernungen_stdAbweichungDesMittelwerts	= getStandartAbweichungDesMittelwerts(entfernungen_stdAbweichung)
        
        # Geschwindigkeiten
        speed_Array									= getSpeedArray(entfernungen_Array, messungNachXms)
        speed_aritMittel							= getArithmetischesMittelFromArray(speed_Array)
        speed_varianzenArray						= getVarianzFromArray(speed_Array, speed_aritMittel)
        speed_stdAbweichung							= getStandartAbweichungFromArray(speed_varianzenArray)
        speed_stdAbweichungDesMittelwerts			= getStandartAbweichungDesMittelwerts(speed_stdAbweichung)
        speed_2Sigma								= get2SigmaFromStdAbweichung(speed_stdAbweichung)

        speed_Array.insert(0, 0)
        
        logger.dump(logger.dumpCSV, i,
                    entfernungen_Array, entfenungen_aritMittel, entfernungen_stdAbweichung, entfernungen_stdAbweichungDesMittelwerts,
                    speed_Array, speed_aritMittel, speed_stdAbweichung, speed_stdAbweichungDesMittelwerts, speed_2Sigma, 
                    init.getMessungsKalibrierFaktor(), aktuelleTemperatur)
        i += 1
        

##############################################################################################################################################
##############################################################################################################################################
if __name__ == "__main__":
    init.initial()
    main()
    

    