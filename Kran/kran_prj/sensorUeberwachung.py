########################################################################################################
# Thread fuer die ueberwachung von der Lichtschranke und dem ReedSchalter
#
# Dieses Modul kontrolliert durchgaengig den Status der beiden Sensoren und
# schreibt diesen in die Variablen lSchranke_ZugErkannt und reedSchalter_ZugErkannt
# Diese Variablen können jederzeit und ohne aufruf von Funktionen wie lichtschrankeUeberwachen()
# durch andere Module genutzt werden
#
# @Status : Getestet Funktioniert
#
########################################################################################################

########################################################################################################
# Importiere von Module
########################################################################################################
import logger
import const
import utime
import _thread
from machine import Pin

########################################################################################################
#    Hier werden die GPIO Pins definiert
########################################################################################################
pin_Lichtschranke	= Pin(const.gpio_LichtschrankeLesen, Pin.IN)
pin_ReedSchalter	= Pin(const.gpio_ReetSchalterLesen, Pin.IN, Pin.PULL_DOWN)

########################################################################################################
#   Globale Variablen
########################################################################################################
stop_flagThread1	 	= False
lSchranke_ZugErkannt 	= 0 # objErkannt == 1 obNichtErkannt == 0
reedSchalter_ZugErkannt	= 0 # objErkannt == 1 obNichtErkannt == 0

########################################################################################################
# Starte den Thread zur Sensorueberwachung auf dem zweiten Pico Kern
# Sobald gestartet wird automatisch die "sensorUeberwachungsLoop gestartet
######################################################################################################## 
def sensorUberwachungStarten():
    _thread.start_new_thread(sensorUberwachungsLoop, ())  
    utime.sleep_ms(10) #Gegen Kernkonflikt
        
########################################################################################################
# Ruft durchgängig die Funktionen zur Lichtschranken- und Reedschalter kontrolle
# in eigener Endlosschleife auf eigenen Pico Kern auf solange die variable
# stop_flagThread1 == False ist.
######################################################################################################## 
def sensorUberwachungsLoop():        
    global stop_flagThread1
    logger.log("Sensor ueberwachungs Thread geastartent", "INFO")
    while not stop_flagThread1:
        lichtschrankeUeberwachen()
        reedSchalterUeberwachen()
        utime.sleep_ms(const.sensorUeberwachungLoopSleepTimeMs) # Entlastung der CPU    
        
########################################################################################################
# Stoppt die Sensor Ueberwachungs Schleife
######################################################################################################## 
def sensorUberwachungStoppen():
    global stop_flagThread1
    logger.log("Sensor ueberwachungs Thread gestoppt", "INFO")
    stop_flagThread1 = True
    utime.sleep(1)        
        
########################################################################################################
# Ueberwacht den Zustand der Lichtschranke und schreibt den
# Status in die Variable lSchranke_ZugErkannt
# Lichtschranke blockiert : lSchranke_ZugErkannt == 1
# Lichtschranke offen : lSchranke_ZugErkannt == 0
#
# Die Log-Meldung soll nur erscheinen, wenn sich der Zustand an der Lichtschranke
# geädnert hat. Nicht durchgängig
#
# ACHTUNG : Die Lichtschranken Hardware HW-201 arbeitet Kabelbruchsicher,
#           dh. muss der Wert am lesenden Pin vom Pico erst gedreht werden
#           eh er in die Variable geschrieben werden kann
# 
######################################################################################################## 
def lichtschrankeUeberwachen():
    global lSchranke_ZugErkannt
    if pin_Lichtschranke.value() != lSchranke_ZugErkannt : return
    if pin_Lichtschranke.value() == 1 : lSchranke_ZugErkannt = 0
    if pin_Lichtschranke.value() == 0 : lSchranke_ZugErkannt = 1
    logger.log(f"Zustandswechsel Lichtschranke lSchranke_ZugErkannt='{lSchranke_ZugErkannt}'", "L-SCHRANKE")


        
########################################################################################################
# Ueberwacht den Zustand des Reed Schalters und schreibt den
# Status in die Variable reedSchalter_ZugErkannt
# Reed Schalter -> 0 Ohm : reedSchalter_ZugErkannt == 1
# Reed Schalter -> unendlich Ohm : reedSchalter_ZugErkannt == 0
#
# Die Log-Meldung soll nur erscheinen, wenn sich der Zustand an der Reed Schalter
# geädnert hat. Nicht durchgängig
# 
######################################################################################################## 
def reedSchalterUeberwachen():
    global reedSchalter_ZugErkannt
    if pin_ReedSchalter.value() == reedSchalter_ZugErkannt : return
    reedSchalter_ZugErkannt = pin_ReedSchalter.value()
    logger.log(f"Zustandswechsel Reed Schalter reedSchalter_ZugErkannt='{reedSchalter_ZugErkannt}'", "Reeed")
