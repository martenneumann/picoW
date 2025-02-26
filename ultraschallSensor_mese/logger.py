import utime
import steuerung

# Initialisiere den Startzeitpunkt, nehme einen Zeitstempel
START_TIME = 0
LETZTER_ZEITSTEMPEL = 0  # Letzter gespeicherter Zeitstempel
dumpCSV 							= 0
dumpHMI								= 1
dumpNurSpeed						= 2

##############################################################################################################################################
# 
##############################################################################################################################################
def setLoggerStartTime():
    global START_TIME, LETZTER_ZEITSTEMPEL
    START_TIME = utime.ticks_ms()
    LETZTER_ZEITSTEMPEL = START_TIME  # Setzt den ersten Vergleichswert

##############################################################################################################################################
# 
##############################################################################################################################################
def zeitStempelAusTicksDiff(t2, t1) :
    gesamtZeit = utime.ticks_diff(t2, t1)
    minutes = gesamtZeit // 60000
    seconds = (gesamtZeit // 1000) % 60
    milliseconds = gesamtZeit % 1000
    return f"{minutes:02}:{seconds:02}.{milliseconds:03}"
    
##############################################################################################################################################
# 
##############################################################################################################################################
def hohleZeitstempel():
    global LETZTER_ZEITSTEMPEL
    aktuellerZeitInUtime = utime.ticks_ms()
    
    aktuellerZeitstempel = zeitStempelAusTicksDiff(aktuellerZeitInUtime, START_TIME)
    differenzZeitstempel = zeitStempelAusTicksDiff(aktuellerZeitInUtime, LETZTER_ZEITSTEMPEL)
    
    LETZTER_ZEITSTEMPEL = aktuellerZeitInUtime
    return aktuellerZeitstempel, differenzZeitstempel

##############################################################################################################################################
# 
##############################################################################################################################################
def dump(dumpForm, durchlauf, entfernungen_Array, entfenungen_aritMittel, entfernungen_stdAbweichung, entfernungen_stdAbweichungDesMittelwerts,
         speed_Array, speed_aritMittel, speed_stdAbweichung, speed_stdAbweichungDesMittelwerts, messungsKalibrierFaktor, aktuelleTemperatur) :
    
    if dumpForm == dumpCSV :
        dumpCsv(dumpHMI, durchlauf, entfernungen_Array, entfenungen_aritMittel, entfernungen_stdAbweichung, entfernungen_stdAbweichungDesMittelwerts,
                speed_Array, speed_aritMittel, speed_stdAbweichung, speed_stdAbweichungDesMittelwerts, messungsKalibrierFaktor, aktuelleTemperatur)
    
    elif dumpForm == dumpHMI :
        dumpHmi(dumpHMI, durchlauf, entfernungen_Array, entfenungen_aritMittel, entfernungen_stdAbweichung, entfernungen_stdAbweichungDesMittelwerts,
                speed_Array, speed_aritMittel, speed_stdAbweichung, speed_stdAbweichungDesMittelwerts, messungsKalibrierFaktor, aktuelleTemperatur)
    
    elif dumpForm == dumpNurSpeed :
        dumpJustSpeed(speed_Array)
##############################################################################################################################################
# 
##############################################################################################################################################
def dumpJustSpeed(speed_Array) :
    for element in speed_Array : print(element)
    
##############################################################################################################################################
# 
##############################################################################################################################################
def dumpHmi(dumpHMI, durchlauf, entfernungen_Array, entfenungen_aritMittel, entfernungen_stdAbweichung, entfernungen_stdAbweichungDesMittelwerts,
            speed_Array, speed_aritMittel, speed_stdAbweichung, speed_stdAbweichungDesMittelwerts, messungsKalibrierFaktor, aktuelleTemperatur) :
    
    
    aktuellerZeitStempel, differenzZeitStempel = hohleZeitstempel()
    print("**********************************************************************************")
    print(f"Durchlauf = [{durchlauf}] || Zeitstempel = [{aktuellerZeitStempel}] || DiverenzZeit = [{differenzZeitStempel}]")
    
    for i, (wert, speed) in enumerate(zip(entfernungen_Array, speed_Array), start=1):
        print(f"Entfernung {i} = [{wert}] cm, Speed = [{speed}] cm/s")
 
    print(f"Ent_Erwartungswert = [{entfenungen_aritMittel}] cm")
    print(f"Ent_StdAbweichung = [{entfernungen_stdAbweichung}] cm")
    print(f"Ent_StdAbweichung des Mittelwerts = [{entfernungen_stdAbweichungDesMittelwerts}] cm")
    
    print(f"Speed_Erwartungswert = [{speed_aritMittel}] cm")
    print(f"Speed_StdAbweichung = [{speed_stdAbweichung}] cm")
    print(f"Speed_StdAbweichung des Mittelwerts = [{speed_stdAbweichungDesMittelwerts}] cm")    
    
    print(f"Messungs Korrektru Faktor = [{messungsKalibrierFaktor}] cm")  
    print(f"Temperatur = [{aktuelleTemperatur}] Celsius")

##############################################################################################################################################
# 
##############################################################################################################################################
def dumpCsv(dumpHMI, durchlauf, entfernungen_Array, entfenungen_aritMittel, entfernungen_stdAbweichung, entfernungen_stdAbweichungDesMittelwerts,
            speed_Array, speed_aritMittel, speed_stdAbweichung, speed_stdAbweichungDesMittelwerts, messungsKalibrierFaktor, aktuelleTemperatur):
    
    aktuellerZeitStempel, differenzZeitStempel = hohleZeitstempel()

    
    if durchlauf == 0:
        head = "DURCHLAUF; AKTUELLE_ZEIT; DIV_ZEIT; "
        for i in range(len(entfernungen_Array)):
            head += f"ENTFERNUNG_{i+1}; SPEED_{i+1}; "  # String-Interpolation mit f-String
        head += "Ent_Erwartungswert; Ent_StdAbweichung; Ent_StdAbweichung; Speed_Erwartungswert; "
        head += "Speed_StdAbweichung; Speed_StdAbweichung_Des_Mittelwerts; Messungs_Korrektur_Faktor; Temperatur"
        print(head)

    log = f"{durchlauf}; {aktuellerZeitStempel}; {differenzZeitStempel}; "
    for i, (wert, speed) in enumerate(zip(entfernungen_Array, speed_Array), start=1):
        log += (f"{wert} ;{speed}; ")
        
    log += f"{entfenungen_aritMittel}; {entfernungen_stdAbweichung};  {entfernungen_stdAbweichungDesMittelwerts}; "
    log += f"{speed_aritMittel}; {speed_stdAbweichung};  {speed_stdAbweichungDesMittelwerts}; "
    log += f"{messungsKalibrierFaktor}; {aktuelleTemperatur};"
    print(log)

    
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

