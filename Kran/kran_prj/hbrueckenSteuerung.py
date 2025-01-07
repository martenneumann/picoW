from machine import Pin, PWM
from machine import Timer
import sensorUeberwachung
import const
import logger
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
def setzeHbrueckenPins(rechts = 0, links = 0):
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
def stoppeZug():
    pin_hBrueckePwm.deinit()
    setzeHbrueckenPins()
    
########################################################################################################
#    
########################################################################################################
#def fahreZugRein(speedInProzent, abbruchzeitInMs):
#    logger.log("Fahre zug in abschnitt REIN", "H_BRUECKE")
#    setzeHbrueckenPins(1, 0) #TODO CHeck ob das so richtig rum ist
#
#    myDutyTime = prozent2dutycycle(speedInProzent)
#    pin_hBrueckePwm.duty_u16(myDutyTime)
# 
#   callback = False 
#    timer1 = Timer(period=abbruchzeitInMs, mode=Timer.ONE_SHOT, callback=stoppeZugViaClk())
#    
#    while reedSchalter_ZugErkannt != 1 :
#        if callback == True : return True       
#    stoppeZugViaReedschalter()

########################################################################################################
#    
########################################################################################################
def fahreZugRein(speedInProzent, abbruchzeitInMs):
    logger.log("Fahre Zug in Abschnitt REIN", "H_BRUECKE")
    setzeHbrueckenPins(1, 0)  # Rechts vorwärts, Links rückwärts

    myDutyTime = prozent2dutycycle(speedInProzent)
    pin_hBrueckePwm.duty_u16(myDutyTime)

    # Kontrollvariable für Timer
    #timer_abgelaufen = [False]

    # Timer initialisieren
    #def timer_callback(timer):
    #    logger.log("Halt durch Timer ausgelöst", "H_BRUECKE")
    #    timer_abgelaufen[0] = True
    #    stoppeZugViaClk()


    #timer1.init(period=abbruchzeitInMs, mode=Timer.ONE_SHOT, callback=timer_callback)

    # Schleife: Warten auf Reed-Schalter oder Timer-Ablauf
    while sensorUeberwachung.reedSchalter_ZugErkannt != 1:
        #if timer_abgelaufen[0]:  # Abbruch durch Timer
        #    return False  # Not-Halt, Zug konnte nicht stoppen
        time.sleep(0.01)  # CPU-Last reduzieren

    stoppeZugViaReedschalter()  # Normaler Halt durch Reed-Schalter
    return True  # Erfolg


########################################################################################################
#    
########################################################################################################
def fahreZugRaus(speedInProzent, abbruchzeitInMs):
    logger.log("Fahre zug in abschnitt RAUS", "H_BRUECKE")
    setzeHbrueckenPins(0, 1) #TODO CHeck ob das so richtig rum ist 

    myDutyTime = prozent2dutycycle(speedInProzent)
    pin_hBrueckePwm.duty_u16(myDutyTime)
 
    # Kontrollvariable für Timer
    #timer_abgelaufen = [False]

    # Timer initialisieren
    #def timer_callback(timer):
    #    logger.log("Timer callback. Wegen sicherheit passiert nicht. Wir warten auf freien Weichenbereich", "H_BRUECKE")
    #    timer_abgelaufen[0] = True
        #stoppeZugViaClk()


    timer1.init(period=abbruchzeitInMs, mode=Timer.ONE_SHOT, callback=timer_callback)
    
    while sensorUeberwachung.lSchranke_ZugErkannt == 0 : # Warte bis zug im Lichtschrankenbereich ist
        #if timer_abgelaufen[0]:  # Abbruch durch Timer
        #return False  # Not-Halt, Zug konnte nicht stoppen
        utime.sleep_ms(50)
    while sensorUeberwachung.lSchranke_ZugErkannt == 1 : # Warte bis zug im Lichtschrankenbereich verlassen hat
        #if timer_abgelaufen[0]:  # Abbruch durch Timer
        #return False  # Not-Halt, Zug konnte nicht stoppen
        utime.sleep_ms(50)
    stoppeZugViaLichtschranke()
