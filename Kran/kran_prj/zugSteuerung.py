########################################################################################################
# Dieses Modul steuert ueber die H-Bruecke L298N den Zug
#
# @Status : Getestet Funktioniert
#
########################################################################################################

########################################################################################################
# Importiere von Module
########################################################################################################

from machine import Pin, PWM
from machine import Timer
import sensorUeberwachung
import simulationsStuff
import const
import logger
import utime
import time


########################################################################################################
#    Hier werden die GPIO Pins definiert
########################################################################################################
pin_hBruecke_ENB	= PWM(Pin(const.gpio_hBrueckeENB))
pin_hBruecke_IN3	= Pin(const.gpio_hBrueckeIn3, Pin.OUT)
pin_hBruecke_IN4	= Pin(const.gpio_hBrueckeIn4, Pin.OUT)


pin_hBruecke_ENB.freq(8) #Setze Frequenz auf 8 Hz (8 Pegel pro Sekunde)
pin_hBruecke_ENB.duty_u16(0)


########################################################################################################
# Rechne einen Prozentwert in eine u16 Zahl um
########################################################################################################
def prozent2dutycycle(percent):
    return int((percent / 100) * 65535)

########################################################################################################
# setze die Richtungspins
#
#@input : in3_OnOrOff = 1 oder 0
#@input : in4_OnOrOff = 1 oder 0
########################################################################################################
def setzeHbrueckenPins(in3_OnOrOff, in4_OnOrOff):
    pin_hBruecke_IN3.value(in3_OnOrOff)
    pin_hBruecke_IN4.value(in4_OnOrOff)

########################################################################################################
# Stoppe das Zugfahren durch ablauf eines Counters    
########################################################################################################
def stoppeZugViaClk():
    logger.log("Stoppe Zug via Timer (Clk)", "H_BRUECKE")
    stoppeZug()
    
########################################################################################################
# Stoppe das Zugfahren durch den Reed Schalter
########################################################################################################
def stoppeZugViaReedschalter():
    logger.log("Stoppe Zug via ReedSchalter", "H_BRUECKE")
    stoppeZug()
    return True

########################################################################################################
# Stoppe das Zugfahren durch die Lichtschranke
########################################################################################################
def stoppeZugViaLichtschranke():
    logger.log("Gleise Stromlos, Zug hat bereich verlassen", "H_BRUECKE")
    stoppeZug()
    return True

########################################################################################################
# Stoppe das Zugfahren durch einen Nutzerinput
########################################################################################################
def stoppeZugViaUserinput():
    print("********************************************************")
    logger.log("Stoppe Zug via User input 'x' ", "H_BRUECKE")
    print("********************************************************")
    stoppeZug()
    return True

########################################################################################################
# Stoppe den Zug
#
# 1. PWM Frequenz am Enable Pin auf 0
# 2. PWM Ueber PWM Lib abschalten
# 3. Richtungs PINs auf aus setzen
#
# ACHTUNG : Trotz aufruf der Funktion konnte trz noch eine Spannung an der H-Bruecke gemessen werden
#
########################################################################################################
def stoppeZug():
    pin_hBruecke_ENB.duty_u16(0)
    pin_hBruecke_ENB.deinit()
    setzeHbrueckenPins(0, 0)


########################################################################################################
# Prüft, ob der Zug basierend auf einer Zeitgrenze gestoppt werden soll.
# 1. Wenn 'abbruchsZeitInMs' 0 ist, wird keine Zeitprüfung durchgeführt.
# 2. Die aktuelle Zeit wird mit 'startZeit' verglichen, und die Differenz wird berechnet.
# 3. Wenn die Zeitdifferenz die 'abbruchsZeitInMs' überschreitet, wird der Zug gestoppt
#    und 'True' zurückgegeben.
# 4. Andernfalls wird 'False' zurückgegeben.
# 
# @input startZeit : Der Zeitpunkt, zu dem der Zug gestartet wurde.
# @input abbruchsZeitInMs : Die Zeit in Millisekunden, nach der der Zug gestoppt
#                           werden soll (0 bedeutet keine abbruchscounter nutzen).
# 
# @return : 'True' wenn der Zug gestoppt wurde, sonst 'False'.
########################################################################################################
def pruefeZugstoppViaClk(startZeit, abbruchsZeitInMs):
    if abbruchsZeitInMs == 0 : return False	#Kein abbruch ueber Zeit erwuenscht
    
    aktuelleZeit = time.ticks_ms()
    zeitDifferenz = time.ticks_diff(aktuelleZeit, startZeit)
    
    if zeitDifferenz >= abbruchsZeitInMs :
        stoppeZugViaClk()
        return True
    else : return False
    
########################################################################################################
# Zug Stoppen durch nutzereingabe
# Wurde durch pruefeAufTestaturEingabe ein "x" eingelesen, stoppe den Zug
#
# @return: True = Zug gestoppt; Flase = Zug nicht gestoppt
#
########################################################################################################
def pruefeZugstoppViaUserinput():    
    tasteVonTastatur = simulationsStuff.pruefeAufTestaturEingabe()
    if tasteVonTastatur == "x" :
        stoppeZugViaUserinput()
        return True
    else : return False    
    
########################################################################################################
# Fahre den Zug in den Kranabschnitt, mit angegebenen Geschwindigkeit, rein 
# und prüft regelmäßig, ob der Zug gestoppt werden soll.
#
# 1. Die Pins für die Brücke werden gesetzt, um die Fahrtrichtung des Zuges
# zu steuern.
# 2. Die Geschwindigkeit des Zuges wird über die Funktion
#    'prozent2dutycycle' in einen Duty Cycle umgerechnet. Ca. 40 Prozent ist die
#     mindestgeschwindigkeit, was Gruppe Stromversorgung fuer uns rausgefunden hat
# 3. Der Zug wird gestartet, und die Startzeit wird erfasst.
# 4. In einer Endlosschleife wird regelmäßig geprüft, ob der Zug gestoppt werden muss:
#    - Über den Reed-Schalter, der den Zug stoppt, wenn er den Punkt erreicht. (Best case)
#    - Über eine Zeitgrenze, die mit 'pruefeZugstoppViaClk' überprüft wird.
#    - Über einen Nutzereingriff, der mit 'pruefeZugstoppViaUserinput' geprüft wird.
# 5. Die Schleife pausiert für 1 Millisekunde, um die CPU-Last zu verringern.
#
# @input speedInProzent : Die Geschwindigkeit des Zuges als Prozentsatz
#                         (Standardwert: const.minZugSpeed).
# @input abbruchsZeitInMs : Die Zeit in Millisekunden, nach der der Zug
#                           gestoppt wird (Standardwert: const.abbruchsZeitInMs_ZugReinfahren).
#
########################################################################################################
def fahreZugRein(speedInProzent = const.minZugSpeed, abbruchsZeitInMs = const.abbruchsZeitInMs_ZugReinfahren):
    logger.log("Fahre Zug in Abschnitt REIN", "H_BRUECKE")
    setzeHbrueckenPins(1, 0)  # Rechts vorwärts, Links rückwärts

    myDutyTime = prozent2dutycycle(speedInProzent)
    pin_hBruecke_ENB.duty_u16(myDutyTime)
    
    startZeit = time.ticks_ms()  # Startzeit erfassen

    while True :
        if sensorUeberwachung.reedSchalter_ZugErkannt == 1:						# Zug stoppen ueber Reed Schlater
            stoppeZugViaReedschalter()
            return 
        if pruefeZugstoppViaClk(startZeit, abbruchsZeitInMs) : return		# Zug stoppen ueber Zeit
        if pruefeZugstoppViaUserinput() : return 								# Zug stoppen ueber Nutzereingriff
        utime.sleep_ms(1)  # CPU-Last reduzieren



########################################################################################################
# Faehrt den Zug in den aus dem Kranabschnitt raus in den Ring zurueck und prüft regelmäßig,
# ob der Zug gestoppt werden muss.
#
# 1. Die Pins für die H-Brücke werden gesetzt, um die Fahrtrichtung des Zuges zu steuern.
# 2. Die Geschwindigkeit des Zuges wird über die Funktion 'prozent2dutycycle' in einen Duty Cycle umgerechnet.
# 3. Die Startzeit wird erfasst, um eine Zeitüberprüfung durchzuführen.
# 4. In der ersten Schleife wird geprüft, ob der Zug im Lichtschrankenbereich erkannt wurde:
#    - Wenn der Zug im Bereich erkannt wird, wird versucht, ihn weiter herauszufahren.
#    - Es wird auch überprüft, ob eine Zeitgrenze überschritten wurde oder ob der Nutzer den Zug gestoppt hat.
# 5. In der zweiten Schleife wird geprüft, ob der Zug den Lichtschrankenbereich verlassen hat:
#    - Wenn ja, wird der Strom auf der H-Brücke abgeschaltet und der Zug gestoppt.
#    - Es wird auch überprüft, ob eine Zeitgrenze überschritten wurde oder ob der Nutzer den Zug gestoppt hat.
#
# @input speedInProzent : Die Geschwindigkeit des Zuges als Prozentsatz
#                         (Standardwert: const.minZugSpeed).
# @input abbruchzeitInMs : Die Zeit in Millisekunden, nach der der Zug gestoppt wird
#                          (Standardwert: const.abbruchsZeitInMs_ZugRausfahren).
#
########################################################################################################

def fahreZugRaus(speedInProzent = const.minZugSpeed, abbruchzeitInMs = const.abbruchsZeitInMs_ZugRausfahren):
    logger.log("Fahre zug in abschnitt RAUS", "H_BRUECKE")
    setzeHbrueckenPins(0, 1) #TODO CHeck ob das so richtig rum ist 

    myDutyTime = prozent2dutycycle(speedInProzent)
    pin_hBruecke_ENB.duty_u16(myDutyTime)
 
    startZeit = time.ticks_ms()  # Startzeit erfassen
    
    while True : 
        if sensorUeberwachung.lSchranke_ZugErkannt == 1 :
            logger.log("Zug im Lichtschranken- / Wichenbereich erkannt, versuche ihn weiter raus zu fahren", "H_BRUECKE")
            break
        if pruefeZugstoppViaClk(startZeit, abbruchzeitInMs) : return
        if pruefeZugstoppViaUserinput() : return
        utime.sleep_ms(50)

    while True :
        if sensorUeberwachung.lSchranke_ZugErkannt == 0 :
            logger.log("Zug hat Lichtschranken- / Wichenbereich verlassen, Strom auf H-Bruecke aus", "H_BRUECKE")
            stoppeZugViaLichtschranke()
            return
        
        if pruefeZugstoppViaClk(startZeit, abbruchzeitInMs) : return
        if pruefeZugstoppViaUserinput() : return
        utime.sleep_ms(50)

    
