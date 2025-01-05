########################################################################################################
#   SG90
#	Braun	= GND
#	Rot		= VCC
#	Gelb	= SIG (Pin 20 GPI15)
########################################################################################################

import logger
import utime
import sensorUeberwachung

# @GEM Weichensteuerung 
from machine import Pin, PWM
from time import sleep

########################################################################################################
#   Globale Variablen
########################################################################################################
weicheAuf				= 1
weicheZu				= 0
# GPIO für Steuersignal
servo_pin 	= 17										# Steuerung des Servos


########################################################################################################
#    Hier werden die GPIO Pins definiert
########################################################################################################
pwm 		= PWM(Pin(servo_pin))							# PWM-Modulatation
pwm.freq(50)										# Frequenz

########################################################################################################
# 
########################################################################################################    
def weicheOeffnen():
    logger.log("Weiche oeffnen", "WEICHE")
    weicheSteuern(weicheAuf)
    
########################################################################################################
# 
########################################################################################################    
def weicheSchliessen():
    logger.log("Weiche schliessen", "WEICHE")
    weicheSteuern(weicheZu)
    
########################################################################################################
# 
########################################################################################################    
def weicheInitalSchliessen():
    logger.log("Stelle sicher das Weiche geschlossen ist", "WEICHE")
    weicheSchliessen()    
    
########################################################################################################
# Code aus mail "micropython Programme" vom 25.09.2024 - 08:20
########################################################################################################    
def weicheSteuern(position):
    #TODO
    if sensorUeberwachung.lSchranke_ZugErkannt == 1 :
        logger.log("Weiche oeffnen erlaubt aber Zug im Weichenbereich. EXIT -1", "ERR")
        sensorUberwachungStoppen()
        exit -1
        
    if position == weicheAuf: pwm.duty_ns(1500000)	# Endanschlag der Weiche, Einlesen der Pulswerte, Stellung des Ruderhorns
    if position == weicheZu : pwm.duty_ns(1300000)	# Weiche links, Endanschlag der Weiche









