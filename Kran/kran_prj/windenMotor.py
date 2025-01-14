########################################################################################################
# Dieses Modul steuert ueber die Treiberplatine ULN 2003 den Schrittmotor 28BYJ-48
#
# ACHTUNG : Grossteil aus dieser Lib entnommen
#           https://github.com/IDWizard/uln2003/blob/master/uln2003.py
#
# @Status : Getestet Funktioniert
#
########################################################################################################

########################################################################################################
# Importiere von Module
########################################################################################################
from machine import Pin
import const
import logger
import time


########################################################################################################
#    Hier werden die GPIO Pins definiert
########################################################################################################
pins_winde = [
    Pin(const.gpio_windenMotorIn1, Pin.OUT),  # IN1
    Pin(const.gpio_windenMotorIn2, Pin.OUT),  # IN2
    Pin(const.gpio_windenMotorIn3, Pin.OUT),  # IN3
    Pin(const.gpio_windenMotorIn4, Pin.OUT),  # IN4
]

########################################################################################################
# Hier werden die Sequenz der 4 Wicklungen im 28BYJ-48 Motor festgelegt,
# so dass immmer der nächste Magnet im Motor greifen kann
# https://github.com/IDWizard/uln2003/blob/master/uln2003.py
# https://ben.akrin.com/driving-a-28byj-48-stepper-motor-uln2003-driver-with-a-raspberry-pi/
########################################################################################################
MOTOR_MAGNET_SEQ = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
]

########################################################################################################
# Diese Funktion setzt die Schrittmotorpins entsprechend der angegebenen Sequenz,
# um den Motor zu bewegen. Die Pins des Motors werden in der Reihenfolge der Sequenz
# geschaltet, um den nächsten Magneten im Motor zu aktivieren und so die Drehung
# des Motors zu steuern.
#
# Zum Verständniss : for pin, value in zip(pins_winde, sequence):
#                    So können in phyon offensichtlich zwei Listen gleichzeitig iteriert werden.
#                    Eig. wird nur die sequence liste auf die pins_winde liste gemaped
# 
# 
# 1. Die Sequenz besteht aus einer Liste von vier Werten, die den Zustand der vier Pins steuern.
# 2. Für jeden Pin in der Sequenz wird der Wert (0 oder 1) auf den entsprechenden Pin ausgegeben.
#
# 
# @input sequence : Eine Liste von vier Werten, die die Wicklungsfolge abbildet
# 
########################################################################################################
def set_step(sequence):
    for pin, value in zip(pins_winde, sequence):
        pin.value(value)

########################################################################################################
# Diese Funktion steuert den Schrittmotor für eine bestimmte Anzahl von Schritten,
# wobei die Richtung und die Verzögerung zwischen den Schritten angepasst werden können.
# 
# 1. Die Anzahl der Schritte wird durch den Parameter 'steps' bestimmt.
# 2. Die Verzögerung zwischen den einzelnen Schritten wird durch den Parameter 'delay' festgelegt.
# 3. Die Richtung des Motors wird durch den Parameter 'direction' festgelegt:
#    - Wenn 'direction' == 1, wird der Motor in Vorwärtsrichtung bewegt.
#    - Wenn 'direction' != 1, wird der Motor in Rückwärtsrichtung bewegt (durch Umkehren der Sequenz).
# 4. In jedem Schritt wird die entsprechende Motorsequenz aktiviert, um den Motor vorwärts oder rückwärts
#    zu bewegen.
# 5. Nach jedem Schritt wird eine Pause gemäß der 'delay' angegebenen Zeit eingelegt, um die Geschwindigkeit
#    des Motors zu steuern.
# 
# @input steps : Die Anzahl der Schritte, die der Motor machen soll.
# @input delay : Die Verzögerung in Sekunden zwischen den einzelnen Schritten.
# @input direction : Die Richtung, in die der Motor bewegt werden soll (1 für vorwärts, anderes für rückwärts).
# 
########################################################################################################
def step_motor(steps, delay, direction):
    for _ in range(steps):
        for step in (MOTOR_MAGNET_SEQ if direction == 1 else reversed(MOTOR_MAGNET_SEQ)):
            set_step(step)
            time.sleep(delay)      

########################################################################################################
# Setze alle Pins für den Motor auf 0
# Motor steht
########################################################################################################
def cleanup():
    set_step([0, 0, 0, 0])


########################################################################################################
# Diese Funktion bewegt den Windenmotor nach oben, um den Harken anzuheben.
# 
# 1. Die Funktion 'step_motor' wird aufgerufen, um den Motor in die definierte Richtung
#    (angegeben durch 'richtungHarkenHoch') zu bewegen, wobei die Anzahl der Schritte und die Verzögerung 
#    entsprechend den Werten in den Konstanten Datei  'stepsHarken' und 'delayHarken' festgelegt sind.
#
# ACHTUNG : Nur Experimentell rausgefunden. Ja nach gewicht am Harken verlaengert sich das
#           Garn oder der Motor "rutscht" mal durch. Auch wie viel Garn abgewickelt ist oder
#           ob das Garn "zufällig" gerade oder schreg gewickelt wird spielt ein große rolle
#
# 3. Nach Abschluss der Bewegung wird die Funktion 'cleanup' um den Motor zu stoppen
# 
# @input steps : Die Anzahl der Schritte, die der Motor machen soll (Standardwert: const.stepsHarken).
# @input speed : Die Verzögerung zwischen den Schritten (Standardwert: const.delayHarken).
# 
########################################################################################################
def fahreHarkenHoch(steps = const.stepsHarken, speed = const.delayHarken) :
    logger.log("Harken hoch fahren", "HARKEN_MOTOR")
    step_motor(steps, speed, const.richtungHarkenHoch)
    cleanup()

########################################################################################################
# Diese Funktion bewegt den Windenmotor nach unten, um den Harken abzulassen.
# 
# 1. Die Funktion 'step_motor' wird aufgerufen, um den Motor in die definierte Richtung
#    (angegeben durch 'richtungHarkenRunter') zu bewegen, wobei die Anzahl der Schritte und die Verzögerung 
#    entsprechend den Werten in den Konstanten Datei  'stepsHarken' und 'delayHarken' festgelegt sind.
#
# ACHTUNG : Nur Experimentell rausgefunden. Ja nach gewicht am Harken verlaengert sich das
#           Garn oder der Motor "rutscht" mal durch. Auch wie viel Garn abgewickelt ist oder
#           ob das Garn "zufällig" gerade oder schreg gewickelt wird spielt ein große rolle
#
# 3. Nach Abschluss der Bewegung wird die Funktion 'cleanup' um den Motor zu stoppen
# 
# @input steps : Die Anzahl der Schritte, die der Motor machen soll (Standardwert: const.stepsHarken).
# @input speed : Die Verzögerung zwischen den Schritten (Standardwert: const.delayHarken).
# 
########################################################################################################
def fahreHarkenRunter(steps = const.stepsHarken, speed = const.delayHarken) :
    logger.log("Harken runter fahren", "HARKEN_MOTOR")
    step_motor(steps, speed, const.richtungHarkenRunter)
    cleanup()
    


    
 

