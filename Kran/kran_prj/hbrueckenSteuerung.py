from machine import Pin
from machine import Timer
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

########################################################################################################
    """
    Wandelt einen Prozentwert in einen 16-Bit-Duty-Wert um.
    
    Args:
        percent (float): Der Duty Cycle in Prozent (0 bis 100).
        
    Returns:
        int: Der Duty Cycle als uint16-Wert (0 bis 65535).
    """  
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
def fahreZugRein(speedInProzent, abbruchzeitInMs):
    logger.log("Fahre zug in abschnitt REIN", "H_BRUECKE")
    setzeHbrueckenPins(1, 0) #TODO CHeck ob das so richtig rum ist

    myDutyTime = prozent2dutycycle(speedInProzent)
    pin_hBrueckePwm.duty_u16(myDutyTime)
 
    callback = False 
    timer1 = Timer(period=abbruchzeitInMs, mode=Timer.ONE_SHOT, callback=stoppeZugViaClk())
    
    while reedSchalter_ZugErkannt != 1 :
        if callback == True : return True       
    stoppeZugViaReedschalter()

########################################################################################################
#    
########################################################################################################
def fahreZugRaus(speedInProzent, abbruchzeitInMs):
    logger.log("Fahre zug in abschnitt RAUS", "H_BRUECKE")
    setzeHbrueckenPins(0, 1) #TODO CHeck ob das so richtig rum ist 

    myDutyTime = prozent2dutycycle(speedInProzent)
    pin_hBrueckePwm.duty_u16(myDutyTime)
 
    callback = False 
    timer1 = Timer(period=abbruchzeitInMs, mode=Timer.ONE_SHOT, callback=stoppeZugViaClk())
    
    while lSchranke_ZugErkannt == 0 : # Warte bis zug im Lichtschrankenbereich ist
        if callback == True : return True
    while lSchranke_ZugErkannt == 1 : # Warte bis zug im Lichtschrankenbereich verlassen hat
        if callback == True : return True
        
    stoppeZugViaLichtschranke()
