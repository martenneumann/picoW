# Bibliotheken laden
from machine import Pin, PWM
from time import sleep
import const
import logger


########################################################################################################
#    Hier werden die GPIO Pins definiert
########################################################################################################
# Servo-PWM initialisieren
pin_turmMotor = PWM(Pin(const.gpio_turmMotor))
pin_turmMotor.freq(50)  # Typische Frequenz für Servos ist 50 Hz

########################################################################################################
# 
########################################################################################################
aktuellerWinkelDesMotors = 500000

########################################################################################################
# 
########################################################################################################
# Funktionen für die Servo-Steuerung
def fahreWinkelAn(winkelInDutyNS):
    pin_turmMotor.duty_ns(winkelInDutyNS)
    sleep(const.verzoegerungTurmMotor)  # Kurze Verzögerung zwischen den Schritten

########################################################################################################
# 
########################################################################################################
def move_smooth(zielWinkel, motorspeed_schrittweite):
    global aktuellerWinkelDesMotors  # Zugriff auf die globale Variable aktuellerWinkelDesMotors
    if aktuellerWinkelDesMotors < zielWinkel:
        for duty in range(aktuellerWinkelDesMotors, zielWinkel + 1, motorspeed_schrittweite):
            fahreWinkelAn(duty)
    else:
        for duty in range(aktuellerWinkelDesMotors, zielWinkel - 1, -motorspeed_schrittweite):
            fahreWinkelAn(duty)
    aktuellerWinkelDesMotors = zielWinkel  # Aktualisierung der globalen Position


########################################################################################################
# 
########################################################################################################
def fahreTurmInPosition1(motorspeed_schrittweite):
    global aktuellerWinkelDesMotors  # Zugriff auf die globale Variable aktuellerWinkelDesMotors
    logger.log("Fahre Turm in Position 1", "TURM")
    move_smooth(const.turmMotorGrad000, motorspeed_schrittweite)
    
########################################################################################################
# 
########################################################################################################
def fahreTurmInPosition2(motorspeed_schrittweite):
    global aktuellerWinkelDesMotors  # Zugriff auf die globale Variable aktuellerWinkelDesMotors
    logger.log("Fahre Turm in Position 2", "TURM")
    move_smooth(const.turmMotorGrad090, motorspeed_schrittweite)        
  
########################################################################################################
# 
########################################################################################################
def fahreTurmInPosition3(motorspeed_schrittweite):
    global aktuellerWinkelDesMotors  # Zugriff auf die globale Variable aktuellerWinkelDesMotors
    logger.log("Fahre Turm in Position 3", "TURM")
    move_smooth(const.turmMotorGrad180, motorspeed_schrittweite)        
      

########################################################################################################
# 
########################################################################################################
def turmMotorAusschalten(motorspeed_schrittweite) :
    logger.log("Fahre Turm in ausgangslage", "TURM")
    fahreTurmInPosition1(motorspeed_schrittweite)
    logger.log("Turmmotor ausschalten (deinit)", "TURM")
    pin_turmMotor.deinit()





