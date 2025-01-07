########################################################################################################
#   SG90
#	Braun	= GND
#	Rot		= VCC
#	Gelb	= SIG (Pin 20 GPI15)
########################################################################################################
import logger
import utime
import const
import sensorUeberwachung

from machine import Pin, PWM
from time import sleep

########################################################################################################
#    Hier werden die GPIO Pins definiert
########################################################################################################
pin_weichenMotor 		= PWM(Pin(const.gpio_weichenMotor))		# PWM-Modulatation
pin_weichenMotor.freq(const.weichenMotorTraegerFrq)				# Traeeger  Frequenz

########################################################################################################
# 
########################################################################################################    
def weicheOeffnen():
    logger.log("Weiche oeffnen", "WEICHE")
    weicheSteuern(const.richtungWeicheAuf)
    
########################################################################################################
# 
########################################################################################################    
def weicheSchliessen():
    logger.log("Weiche schliessen", "WEICHE")
    weicheSteuern(const.richtungWeicheZu)
    
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
        #sensorUberwachungStoppen()
        #exit -1
        
    if position == const.richtungWeicheAuf: pin_weichenMotor.duty_ns(const.endlageWeicheAuf)	# Weiche auffahren
    if position == const.richtungWeicheZu : pin_weichenMotor.duty_ns(const.endlageWeicheZu)		# Weiche zufahren








