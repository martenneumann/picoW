# Bibliotheken laden
import steuerung
import sensoren

aktuelleTemperatur = 0

##########################################################################################################################################
# 
##########################################################################################################################################
def userAbfrage() :
    #kalibrierungsstrategie = input("Kalibrierstrategie : 1 - Einpunkt, 2 - Zweipunkt ")
    #if kalibrierungsstrategie == "1" : return float(input("Gebe die entfernung in cm an auf die Genullt werden soll "))
    #kalPunktEins = float(input("Gebe den ersten Punkt an auf den Kalibriert werden soll "))
    #return kalPunktEins, float(input("Gebe den zweiten Punkt an auf den Kalibriert werden soll "))
    return 50

##########################################################################################################################################
# 
##########################################################################################################################################
def kallibrierungsMessung() :
    input("Taste druecken fuer Messung")
    steuerung.setEntfernungsArray(aktuelleTemperatur)
    return steuerung.getArithmetischesMittelFromMessungsArray()
        
##########################################################################################################################################
# 
##########################################################################################################################################
def getMessungsKorekturFaktor1Punkt(kalibrierungspunkt_nutzer) :
    arithmetischesMittel_KalkPunktEins = kallibrierungsMessung()
    return 1 / (arithmetischesMittel_KalkPunktEins / kalibrierungspunkt_nutzer), arithmetischesMittel_KalkPunktEins
        
##########################################################################################################################################
# 
##########################################################################################################################################
def getMessungsKorekturFaktor2Punkte(kalibrierungspunkt_nutzerEins, kalibrierungspunkt_nutzerZwei) :
    arithmetischesMittel_KalkPunktEins = kallibrierungsMessung()
    arithmetischesMittel_KalkPunktZwei = kallibrierungsMessung()
    retVal = 1 /  ((arithmetischesMittel_KalkPunktZwei - arithmetischesMittel_KalkPunktEins) / (kalibrierungspunkt_nutzerZwei - kalibrierungspunkt_nutzerEins))
    return retVal, arithmetischesMittel_KalkPunktEins, arithmetischesMittel_KalkPunktZwei
        
##########################################################################################################################################
# 
##########################################################################################################################################
def dumpInit2Punkte(kalibrierungspunkt, kalPunktEins, kalPunktZwei):
    print("*****************************************************************************")
    print("START DUMP INITIALISIERUNG")
    print("Es wird an Zwei Positionen gemessen")
    print(f"Position 1 Sollwert x1 =		({kalibrierungspunkt[0]})")
    print(f"Position 2 Sollwert x2 =		({kalibrierungspunkt[1]})")
    print(f"Position 1 Echterwert y1 =	({kalPunktEins})")
    print(f"Position 2 Echterwert y2 =	({kalPunktZwei})")
    print("Berechnungsformel			(y2 - y1) / (x1 - x2)")
    print(f"Die Steigung betraegt    	({1 * kalibrierungspunkt[1]})")
    print(f"Der Kalibrierungsfaktor ist	({kalibrierungspunkt})")
    print("ENDE DUMP INITIALISIERUNG")
    print("*****************************************************************************")

        
#########################################################################################################################################
# 
##########################################################################################################################################
def dumpInit1Punkt(kalibrierungspunkt, kalPunktEins):
    print(f"*****************************************************************************")
    print(f"START DUMP INITIALISIERUNG")
    print(f"Es wird an einer Position gemessen")
    print(f"Position 1 Sollwert x =		({kalibrierungspunkt})")
    print(f"Position 1 Echterwert y =	({kalPunktEins})")  # Korrektur hier
    print(f"Berechnungsformel			(y / x)")
    print(f"Die Steigung betraegt    	({1 * kalibrierungspunkt})")
    print(f"Der Kalibrierungsfaktor ist	({kalibrierungspunkt})")
    print(f"ENDE DUMP INITIALISIERUNG")
    print(f"*****************************************************************************")

        
##############################################################################################################################################
# 
##############################################################################################################################################
def initial() :
    kalibrierungspunkte = userAbfrage()
    aktuelleTemperatur = sensoren.getTemperatur()
    
    if isinstance(kalibrierungspunkte, tuple) :
        messungsKorrekturFaktor, kalPunktEins, kalPunktZwei = getMessungsKorekturFaktor2Punkte(kalibrierungspunkte[0], kalibrierungspunkte[1])
        dumpInit2Punkte(kalibrierungspunkte, kalPunktEins, kalPunktZwei)
    else :
        messungsKorrekturFaktor, kalPunktEins = getMessungsKorekturFaktor1Punkt(kalibrierungspunkte)
        dumpInit1Punkt(kalibrierungspunkte, kalPunktEins)
        
    steuerung.setMessungsKorrekturFaktor(messungsKorrekturFaktor)
    messungs_Array = []