from machine import Pin, PWM
from machine import Timer
import sensorUeberwachung
import const
import logger
import simulationsStuff
import time

########################################################################################################
#    Hier werden die GPIO Pins definiert
########################################################################################################
pin_hBrueckePwm		= PWM(Pin(const.gpio_hBrueckePwm))
pin_hBrueckeRechts	= Pin(const.gpio_hBrueckeRechts, Pin.OUT)
pin_hBrueckeLinks	= Pin(const.gpio_hBrueckeLinks, Pin.OUT)


pin_hBrueckePwm.freq(8) #Setze Frequenz auf 8 Hz (8 Pegel pro Sekunde)
#timer1 = Timer(0)

########################################################################################################
#
########################################################################################################
def prozent2dutycycle(percent):
    return int((percent / 100) * 65535)

########################################################################################################
#    
########################################################################################################
def setzeHbrueckenPins(rechts, links):
    pin_hBrueckeRechts.value(rechts)
    pin_hBrueckeLinks.value(links)

########################################################################################################
#    
########################################################################################################
def stoppeZugViaClk():
    logger.log("Stoppe Zug via Timer (Clk)", "H_BRUECKE")
    stoppeZug()
    
########################################################################################################
#    
########################################################################################################
def stoppeZugViaReedschalter():
    logger.log("Stoppe Zug via ReedSchalter", "H_BRUECKE")
    stoppeZug()
    return True

########################################################################################################
#    
########################################################################################################
def stoppeZugViaLichtschranke():
    logger.log("Gleise Stromlos, Zug hat bereich verlassen", "H_BRUECKE")
    stoppeZug()
    return True

########################################################################################################
#    
########################################################################################################
def stoppeZugViaUserinput():
    logger.log("Stoppe Zug via User input 'x' ", "H_BRUECKE")
    stoppeZug()
    return True

########################################################################################################
#    
########################################################################################################
def stoppeZug():
    pin_hBrueckePwm.deinit()
    setzeHbrueckenPins(0, 0)
    
########################################################################################################
#    
########################################################################################################
def pruefeZugstoppViaClk(startZeit):
    aktuelleZeit = time.ticks_ms()
    zeitDifferenz = time.ticks_diff(aktuelleZeit, startZeit)
    
    if zeitDifferenz >= abbruchsZeitInMs :
        stoppeZugViaClk()
        return True
    else : return False
    
########################################################################################################
#    
########################################################################################################
def pruefeZugstoppeViaUserinput():    
    tasteVonTastatur = simulationsStuff.pruefeAufTestaturEingabe()
    if tasteVonTastatur == "x" :
        stoppeZugViaUserinput()
        return True
    else : return False    
    
########################################################################################################
#    
########################################################################################################
def fahreZugRein(speedInProzent, abbruchsZeitInMs):
    logger.log("Fahre Zug in Abschnitt REIN", "H_BRUECKE")
    setzeHbrueckenPins(1, 0)  # Rechts vorwärts, Links rückwärts

    myDutyTime = prozent2dutycycle(speedInProzent)
    pin_hBrueckePwm.duty_u16(myDutyTime)
    
    startZeit = time.ticks_ms()  # Startzeit erfassen

    while True :
        # Zug stoppen ueber Reed Schlater
        if sensorUeberwachung.reedSchalter_ZugErkannt == 1:
            stoppeZugViaReedschalter()
            return 
        
        # Zug stoppen ueber Zeit
        if pruefeZugstoppViaClk() : return
                
        # Zug stoppen ueber Nutzereingriff
        if pruefeZugstoppeViaUserinput() : return

        time.sleep(0.01)  # CPU-Last reduzieren



########################################################################################################
#    
########################################################################################################
def fahreZugRaus(speedInProzent, abbruchzeitInMs):
    logger.log("Fahre zug in abschnitt RAUS", "H_BRUECKE")
    setzeHbrueckenPins(0, 1) #TODO CHeck ob das so richtig rum ist 

    myDutyTime = prozent2dutycycle(speedInProzent)
    pin_hBrueckePwm.duty_u16(myDutyTime)
 
    startZeit = time.ticks_ms()  # Startzeit erfassen
    
    # Warte bis zug im Lichtschrankenbereich ist
    # mit alternativen abbruchsmoeglichkeiten
    while True : 
        # Erkenne Zug im Lichtschrankenbereich
        if sensorUeberwachung.lSchranke_ZugErkannt == 1 :
            logger.log("Zug im Lichtschranken- / Wichenbereich erkannt, versuche ihn weiter raus zu fahren", "H_BRUECKE")
            break
        # Zug stoppen ueber Zeit
        if pruefeZugstoppViaClk() : return
        # Zug stoppen ueber Nutzereingriff
        if pruefeZugstoppeViaUserinput() : return
                
        utime.sleep_ms(50)

    # Warte bis zug ausserhalb des Lichtschrankenbereich ist
    # mit alternativen abbruchsmoeglichkeiten
    while True :
        # Erkenne Zug im Lichtschrankenbereich
        if sensorUeberwachung.lSchranke_ZugErkannt == 0 :
            logger.log("Zug hat Lichtschranken- / Wichenbereich verlassen, Strom auf H-Bruecke aus", "H_BRUECKE")
            stoppeZugViaLichtschranke()
            return
        
        # Zug stoppen ueber Zeit
        if pruefeZugstoppViaClk() : return
        # Zug stoppen ueber Nutzereingriff
        if pruefeZugstoppeViaUserinput() : return
                
        utime.sleep_ms(50)

    
