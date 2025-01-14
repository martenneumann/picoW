########################################################################################################
# Dieses Modul steuert den Weichenmotor SG90
#
# @Status : Getestet Funktioniert
#
########################################################################################################

########################################################################################################
# Importiere von Module
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
# Oeffnet die Weiche
########################################################################################################    
def weicheOeffnen():
    logger.log("Weiche oeffnen", "WEICHE")
    weicheSteuern(const.endlageWeicheAuf)
    
########################################################################################################
# Schließt die Weiche
########################################################################################################    
def weicheSchliessen():
    logger.log("Weiche schliessen", "WEICHE")
    weicheSteuern(const.endlageWeicheZu)
    
########################################################################################################
# Oeffnet die Weiche Initial
# Soll bei Programmstart aufgerufen werden
########################################################################################################    
def weicheInitalSchliessen():
    logger.log("Stelle sicher das Weiche geschlossen ist", "WEICHE")
    weicheSteuern(const.endlageWeicheZu)    
    
########################################################################################################
# Weichen Motor bewegen auf einen bestimmt Winkel
#
# 1. Ueberpruefe dass kein gegenstand die Lichtschranke unterbricht.
#    (Zug im Weichenbereich)
# 2. Weiche faehrt Winkel an
#
# @input = Weichenwinkel als PWM duty
#
########################################################################################################    
def weicheSteuern(position):
    if sensorUeberwachung.lSchranke_ZugErkannt == 1 :
        logger.log("Weiche steuern erlaubt aber Zug im Weichenbereich. EXIT -1", "ERR")
        sensorUberwachungStoppen()
        exit -1
        
    pin_weichenMotor.duty_ns(position)









