# Bibliotheken laden
from machine import Pin
from time import sleep, sleep_us, ticks_us

##############################################################################################################################################
#Config
##############################################################################################################################################
unglueltigeMessungZeit 		= 200000 													#Mikrosekunden
adiabatenexponent 			= 1.402														# Adiabatenexponent für trockene Luft
universelle_gaskonstante 	= 8.3145  													# J/(mol·K)
molare_masse_luft 			= 0.02896  													# kg/mol
id 							= 0
trigger 					= Pin(16, Pin.OUT)											# Initialisierung GPIO-Ausgang für Trigger-Signal
echo 						= Pin(17, Pin.IN)											# Initialisierung GPIO-Eingang für Echo-Signal
temperatur 					= int(input("Gib die aktuelle Temperatur in Celsius ein: "))
userOffset	 					= int(input("Gib den gewünschten Offset in cm ein: "))
alleMessungen_array = []

##############################################################################################################################################
# Returned die aktuelle Temperatur. Aktuell nach User eingabe
##############################################################################################################################################
def getTemperatur():
    return temperatur

##############################################################################################################################################
# Returned den Gewünschten Offset. Gerade nach User eingabe
##############################################################################################################################################
def getUserOffset():
    return Useroffset


##############################################################################################################################################
# https://www.mikrocontroller.net/attachment/218122/HC-SR04_ultraschallmodul_beschreibung_3.pdf
# 1. Das Auslösen eines Messzyklus geschieht durch eine fallende Flanke am Triggereingang (Pin 2 == trigger) für mindestens 10µs.
#    Darufhin wird ein Tonsignal gesendet
# 2. Danach geht der Ausgang (Echo, Pin 3 == echo) sofort auf H-Pegel und das Modul wartet auf den Empfang des Echos.
#    d.h. Checken wir in der ersten While ob der Pin bereits auf H ist, solange holen wir uns immer wieder den Zeitstempel
#    sobald Pin == 1 ist der letzte gespeicherte Zeitstempel die Zeit in der wir das Signal losgeschickt haben 
# 3. Wird dieses detektiert fällt der Ausgang auf L-Pegel 
#    d.h in der zweiten While checken wir ob das Signal angekommen ist == L Pegel. Solange es nicht angekommen ist speichern wir 
#    kontiuirlich den Zeitstempel. Sobald While verlassen ist der letzt gespeicherte Zeitstempel die ankunftszeit des Signals
# 4. Wird kein Echo detektiert verweilt der Ausgang für insgesamt 200ms auf H-Pegel und zeigt so die erfolglose Messung an.
#	 In diesem Fall returnen wir den dritten Parameter als false
##############################################################################################################################################
def getStartEndLaufzeiten():
    # Erzeuge Flanke
    trigger.low()
    sleep_us(2)
    trigger.high()
    sleep_us(5)
    trigger.low()	
    # Zeitmessungen
    while echo.value() == 0:
       signalGesendetZeitstempel = ticks_us()
    while echo.value() == 1:         
       signalEmpfangenZeitstempel = ticks_us()

    #Ungültige Messung	
    if signalEmpfangenZeitstempel - signalGesendetZeitstempel >= unglueltigeMessungZeit:
        return signalGesendetZeitstempel, signalEmpfangenZeitstempel, False

    return signalGesendetZeitstempel, signalEmpfangenZeitstempel, True



##############################################################################################################################################
# Gibt die Schallgeschwindigkeit in Luft als ideales Gas zurück
# ACHTUNG: Luftdruck und Feuchtigkeit werden nicht bekrücksichtigt
# https://de.wikipedia.org/wiki/Schallgeschwindigkeit#Schallgeschwindigkeit_im_idealen_Gas
##############################################################################################################################################	
def getSchallgeschwindigkeit():

    # Temperatur in Kelvin umrechnen
    temperatur_kelvin = getTemperatur() + 273.15

    # Schallgeschwindigkeit berechnen
    schallgeschwindigkeit = (adiabatenexponent * universelle_gaskonstante * temperatur_kelvin / molare_masse_luft) ** 0.5

    return schallgeschwindigkeit 

##############################################################################################################################################
# 
##############################################################################################################################################	
def getEntfernung(tonLaufzeit):
    doppelteStrecke = tonLaufzeit * getSchallgeschwindigkeit()
    einfacheStrecke = doppelteStrecke / 2
    return einfacheStrecke

##############################################################################################################################################
# Header um CSV datei auf console auszugeben
##############################################################################################################################################
def dumpCsvHeader():
    print("ID, StreckeMitOffset, StreckeAbsolut, TonLaufzeit, Temperatur, UserOffset, ZeitGesendet, ZeitEmpfangen, MessungErfolgreich")

##############################################################################################################################################
# Werte als CSV datei auf console auszugeben
##############################################################################################################################################
def dumpWerte(data):
    #print(data[0] + ";" + data[1] + ";" + data[2] + ";" + data[3] + ";" + data[4] + ";" + data[5]  + ";" + data[6] + ";" + data[7])
    print(",".join(map(str, data)))

##############################################################################################################################################
# 
##############################################################################################################################################
def kalibrierungsMessung():
    kalibrierungsMessungen_array = []  # Initialisierung der Liste
    print("Messung, Strecke")
    for i in range(15):
        zeitstempel = getStartEndLaufzeiten()
        if zeitstempel[2] == True:
            tonLaufzeit 	= zeitstempel[1] - zeitstempel[0]
            absoluteStrecke = getEntfernung(tonLaufzeit)
            kalibrierungsMessungen_array.append(absoluteStrecke)  # Hinzufügen zur Liste
            print(str(i) + "," + str(absoluteStrecke))
        sleep(1)    

    # Berechne den Mittelwert der Messungen
    arithmetischesMittel = sum(kalibrierungsMessungen_array) / len(kalibrierungsMessungen_array)

    # Berechne die Summe der quadrierten Abweichungen
    squared_diff_sum = 0
    for x in kalibrierungsMessungen_array:
        squared_diff_sum += (x - arithmetischesMittel) ** 2

    # Berechne die Varianz
    variance = squared_diff_sum / len(kalibrierungsMessungen_array)

    # Berechne die Standardabweichung
    std_dev = math.sqrt(variance)

    # Berechne den Offset
    offset = arithmetischesMittel - getUserOffset()  # Der Unterschied zwischen dem Mittelwert und dem gewünschten Offset
    
    print(f"Mittelwert der Messungen: {mean} cm")
    print(f"Standardabweichung: {std_dev} cm")
    print(f"Berechneter Offset: {offset} cm")

    # Gib den kalibrierten Wert (Mittelwert + Offset) aus
    return offset
    
            
##############################################################################################################################################
# Init
##############################################################################################################################################
dumpCsvHeader()

##############################################################################################################################################
##############################################################################################################################################
# Wiederholung (Endlos-Schleife)
while True:

    zeitstempel			= getStartEndLaufzeiten()
    tonLaufzeit 		= zeitstempel[1] - zeitstempel[0]
    streckeAbsolut		= getEntfernung(tonLaufzeit)
    streckeMitOffset	= streckeAbsolut - getUserOffset()

    aktuelleMessung = [id, streckeMitOffset, streckeAbsolut, tonLaufzeit, getTemperatur(), getUserOffset(), zeitstempel[0], zeitstempel[1], zeitstempel[2]] 
    alleMessungen_array.append(aktuelleMessung)
    
    dumpWerte(aktuelleMessung)

    id += 1
    sleep(3)


