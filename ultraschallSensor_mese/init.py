# Bibliotheken laden
import steuerung
import sensoren
import logger
from time import sleep

messungsKalibrierFaktor = 0

##########################################################################################################################################
# 
##########################################################################################################################################
def kallibrierungsMessung() :
    input("Taste druecken fuer Messung")
    messungs_Array = []
    aktuelleTemperatur = sensoren.getTemperatur()
    messungs_Array = steuerung.getEntfernungsArray(aktuelleTemperatur)
    logger.dumpKalibrierungsMessungAlleWerte(messungs_Array) 
    return steuerung.getArithmetischesMittelFromArray(messungs_Array)
        
##########################################################################################################################################
# 
##########################################################################################################################################
def getMessungsKorekturFaktor(kalibrierungspunkt_nutzer) :
    arithmetischesMittel_KalkPunkt = kallibrierungsMessung()
    return float((kalibrierungspunkt_nutzer - arithmetischesMittel_KalkPunkt)), arithmetischesMittel_KalkPunkt
        
##############################################################################################################################################
# 
##############################################################################################################################################
def getMessungsKalibrierFaktor() :
    global messungsKalibrierFaktor
    return float(messungsKalibrierFaktor)

##########################################################################################################################################
# 
##########################################################################################################################################
def getKallibrierungspunktFromUser() :
    return float(input("Auf welchen Punkt in cm soll Kalibriert werden "))

    
##############################################################################################################################################
# 
##############################################################################################################################################
def initial() :
    global messungsKalibrierFaktor
    kalibrierungspunkte_User = getKallibrierungspunktFromUser()
    messungsKalibrierFaktor, aritMittelMessung = getMessungsKorekturFaktor(kalibrierungspunkte_User)
    logger.dumpInit(kalibrierungspunkte_User, aritMittelMessung, messungsKalibrierFaktor)
    sleep(1)
    logger.setLoggerStartTime()



