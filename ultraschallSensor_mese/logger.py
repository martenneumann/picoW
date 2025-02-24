import utime
import steuerung

# Initialisiere den Startzeitpunkt, nehme einen Zeitstempel
START_TIME = utime.ticks_ms()

##############################################################################################################################################
# 
##############################################################################################################################################
def hohleZeitstempel():
    sysZeit = utime.ticks_diff(utime.ticks_ms(), START_TIME)
    minutes = sysZeit // 60000
    seconds = (sysZeit // 1000) % 60
    milliseconds = sysZeit % 1000
    return f"{minutes:02}:{seconds:02}.{milliseconds:03}"

##############################################################################################################################################
# 
##############################################################################################################################################
def dump(dumpForm, durchlauf, messungs_Array, messungs_korregiert_Array, aritMittel, stdAbweichung, speed, messungsKorrekturFaktor, aktuelleTemperatur) :
    if dumpForm == 0 :
        dumpCsv(durchlauf, messungs_Array, messungs_korregiert_Array, aritMittel, stdAbweichung, speed, messungsKorrekturFaktor, aktuelleTemperatur)
    elif dumpForm == 1 :
        dumpHmi(durchlauf, messungs_Array, messungs_korregiert_Array, aritMittel, stdAbweichung, speed, messungsKorrekturFaktor, aktuelleTemperatur)
    elif dumpForm == 2 :
        dumpJustSpeed(speed)
##############################################################################################################################################
# 
##############################################################################################################################################
def dumpJustSpeed(speed) :
    print(f"Geschwindigkeit = [{speed}] cm/s")
    
##############################################################################################################################################
# 
##############################################################################################################################################
def dumpHmi(durchlauf, messungs_Array, messungs_korregiert_Array, aritMittel, stdAbweichung, speed, messungsKorrekturFaktor, aktuelleTemperatur) :
    zeitStempel = hohleZeitstempel()
    print("**********************************************************************************")
    print(f"Durchlauf = [{durchlauf}] || Zeitstempel = [{zeitStempel}]")
    
    for i, (wert, korregiert) in enumerate(zip(messungs_Array, messungs_korregiert_Array), start=1):
        print(f"Rohwert {i} = [{wert}] cm | Korrigiert = [{korregiert}] cm")
 
    print(f"Messungs Korrektru Faktor = [{messungsKorrekturFaktor}] cm")    
    print(f"Erwartungswert = [{aritMittel}] cm")
    print(f"Abweichung = [{stdAbweichung}] cm")
    print(f"Geschwindigkeit = [{speed}] cm/s")
    print(f"Temperatur = [{aktuelleTemperatur}] Celsius")

##############################################################################################################################################
# 
##############################################################################################################################################
def dumpCsv(durchlauf, messungs_Array, messungs_korregiert_Array, aritMittel, stdAbweichung, speed, messungsKorrekturFaktor, aktuelleTemperatur):
    zeitStempel = hohleZeitstempel()
    
    if durchlauf == 0:
        print("DURCHLAUF; ZEIT_STEMPEL; " + 
              "; ".join([f"MES{i+1}" for i in range(10)]) + "; " +
              "; ".join([f"MES_KOR{i+1}" for i in range(10)]) + "; " +
              "MESS_KOR_FAKTOR; ERWARTUNG; ABWEICHUNG; SPEED; TEMP")
    
    row = (
        [durchlauf, zeitStempel] +
        list(messungs_Array if messungs_Array else [None] * 10) +
        list(messungs_korregiert_Array if messungs_korregiert_Array else [None] * 10) +
        [messungsKorrekturFaktor, 
         aritMittel,  
         stdAbweichung,  
         speed, aktuelleTemperatur]
    )
    
    print("; ".join(map(str, row)))  # Verwende Semikolon als Trennzeichen
    
##########################################################################################################################################
# 
##########################################################################################################################################
def dumpKalibrierungsMessungAlleWerte(messungs_Array) :
    print("*****************************************************************************")
    print("ROHWERTE DER KALLIBRIERUNGS MESSUNG")
    for i, element in enumerate(messungs_Array):
        print(f"Messung {i} = ({element}) cm")

#########################################################################################################################################
# 
##########################################################################################################################################
def dumpInit(kalibrierungspunkte_User, kalPunktEins, messungsKorrekturFaktor):
    print(f"*****************************************************************************")
    print(f"START DUMP INITIALISIERUNG")
    print(f"Es wird an einer Position gemessen")
    print(f"Position 1 Sollwert x		= ({kalibrierungspunkte_User})")
    print(f"Position 1 Echterwert y		= ({kalPunktEins})")  # Korrektur hier
    print(f"Berechnungsformel			= (x - y)")
    print(f"Der Kalibrierungsfaktor ist	= ({messungsKorrekturFaktor})")
    print(f"ENDE DUMP INITIALISIERUNG")
    print(f"*****************************************************************************")
