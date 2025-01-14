########################################################################################################
# Modul um den Ausleger des Krans zu steuern
#
# @Status : Getestet Funktioniert
#
########################################################################################################

########################################################################################################
# Importiere von Module
########################################################################################################

from machine import Pin, PWM
from time import sleep
import const
import logger


########################################################################################################
#    Hier werden die GPIO Pins definiert
########################################################################################################
pin_turmMotor = PWM(Pin(const.gpio_turmMotor)) #Pn als PWM Pin festlegen
pin_turmMotor.freq(50)  # Typische Frequenz für Servos ist 50 Hz

########################################################################################################
# Setze Initial den aktuellen Winkel auf 0 Grad was der ausgangsposition entspricht
########################################################################################################
aktuellerWinkelDesMotors = const.turmMotorGrad000

########################################################################################################
# Fährt den Winkel an. Winkel wird dem Motor ueber PWM Signal mitgeteilt
#
# @input : winkelInDutyNS = Winkel der angefahren werden soll als ns duty PWM signal
#
########################################################################################################
def fahreWinkelAn(winkelInDutyNS):
    pin_turmMotor.duty_ns(winkelInDutyNS) # Funktionen für die Servo-Steuerung
    sleep(const.verzoegerungTurmMotor)    # Kurze Verzögerung zwischen den Schritten

########################################################################################################
# Funktion bewegt den Turm Motor von seinem aktuellen Winkel zu einem Zielwinkel mit einer
# konstanten Schrittweite, dies soll fuer eine gleichmaesige geschwindigkeit sorgen.
# (Ruckelt trz ein wenig, schon an allen Werten gespielt)
# 
# 1. Zugriff auf die globale Variable 'aktuellerWinkelDesMotors', um die aktuelle Position des Motors
#    zu kennen.
# 2. Überprüft, ob der Zielwinkel größer oder kleiner als der
#    aktuelle Winkel ist.
# 3. Wenn der Zielwinkel größer ist, wird der Motor schrittweise
#    in Richtung Zielwinkel bewegt. Der Motor wird in Schritten der Größe
#   'motorspeed_schrittweite' weiter richtung Zielwinkel gestellt.
# 4. Wenn der Zielwinkel kleiner ist, wird der Motor schrittweise in die entgegengesetzte Richtung
#    bewegt, ebenfalls in Schritten der Größe 'motorspeed_schrittweite'.
# 5. Nach Abschluss der Bewegung wird die globale Variable 'aktuellerWinkelDesMotors' auf den Zielwinkel
#    gesetzt, um die Position zu aktualisieren.
# 
# @input zielWinkel : Der Zielwinkel, zu dem der Motor bewegt werden soll.
# @input motorspeed_schrittweite : Die Schrittweite des Motors das Tempo.
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
# Fahre den Turmmotor in ausgangsposition 1 (0 Grad)
#
# @input motorspeed_schrittweite : Die Schrittweite des Motors das Tempo.
#
########################################################################################################
def fahreTurmInPosition1(motorspeed_schrittweite):
    global aktuellerWinkelDesMotors  # Zugriff auf die globale Variable aktuellerWinkelDesMotors
    logger.log("Fahre Turm in Position 1", "TURM")
    move_smooth(const.turmMotorGrad000, motorspeed_schrittweite)
    
########################################################################################################
# Fahre den Turmmotor in Position 2 "Beladen" (90 Grad)
#
# @input motorspeed_schrittweite : Die Schrittweite des Motors das Tempo.
#
########################################################################################################
def fahreTurmInPosition2(motorspeed_schrittweite):
    global aktuellerWinkelDesMotors  # Zugriff auf die globale Variable aktuellerWinkelDesMotors
    logger.log("Fahre Turm in Position 2", "TURM")
    move_smooth(const.turmMotorGrad090, motorspeed_schrittweite)        
  
########################################################################################################
# Fahre den Turmmotor in Position 3 "Entladen" (180 Grad)
#
# @input motorspeed_schrittweite : Die Schrittweite des Motors das Tempo.
#
########################################################################################################
def fahreTurmInPosition3(motorspeed_schrittweite):
    global aktuellerWinkelDesMotors  # Zugriff auf die globale Variable aktuellerWinkelDesMotors
    logger.log("Fahre Turm in Position 3", "TURM")
    move_smooth(const.turmMotorGrad180, motorspeed_schrittweite)        
      

########################################################################################################
# Schalte den Turmmotor aus
# 1. Fahre den Turmmotor in ausgangsposition 1 (0 Grad)
# 2. Nehme das PWM Signal weg
#
# @input motorspeed_schrittweite : Die Schrittweite des Motors das Tempo.
#
########################################################################################################
def turmMotorAusschalten(motorspeed_schrittweite) :
    logger.log("Fahre Turm in ausgangslage", "TURM")
    fahreTurmInPosition1(motorspeed_schrittweite)
    logger.log("Turmmotor ausschalten (deinit)", "TURM")
    pin_turmMotor.deinit()





