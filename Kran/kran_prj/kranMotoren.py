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

pins_turm = [
    Pin(const.gpio_turmMotorIn1, Pin.OUT),  # IN1
    Pin(const.gpio_turmMotorIn2, Pin.OUT),  # IN2
    Pin(const.gpio_turmMotorIn3, Pin.OUT),  # IN3
    Pin(const.gpio_turmMotorIn4, Pin.OUT),  # IN4
]

# Sequenz für den ULN2003 (Halbschrittmodus)
SEQUENCE = [
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
# 
########################################################################################################
def set_step(pins, sequence):
    for pin, value in zip(pins, sequence):
        pin.value(value)

########################################################################################################
# 
########################################################################################################
def step_motor(pin, steps, delay, direction):
    for _ in range(steps):
        for step in (SEQUENCE if direction == 1 else reversed(SEQUENCE)):
            set_step(pin, step)
            time.sleep(delay)      

########################################################################################################
# 
########################################################################################################
def cleanup(pin):
    set_step(pin, [0, 0, 0, 0])

########################################################################################################
# 
########################################################################################################
def fahreHarkenHoch() :
    logger.log("Harken runter fahren", "HARKEN_MOTOR")
    step_motor(pins_winde, const.stepsHarken, const.delayHarken, const.richtungHarkenHoch)
    cleanup(pins_winde)

########################################################################################################
# 
########################################################################################################
def fahreHarkenRunter() :
    logger.log("Harken hoch fahren", "HARKEN_MOTOR")
    step_motor(pins_winde, const.stepsHarken, const.delayHarken, const.richtungHarkenRunter)
    cleanup(pins_winde)

########################################################################################################
# 
########################################################################################################
def rotiereTurmLinks() :
    logger.log("Rotiere Turm Links", "TURM_MOTOR")
    step_motor(pins_turm, const.stepsTurm, const.delayTurm, const.richtungTurmDrehtLinks)
    cleanup(pins_turm)       

########################################################################################################
# 
########################################################################################################
def rotiereTurmRecht() :
    logger.log("Rotiere Turm Rechts", "TURM_MOTOR")
    step_motor(pins_turm, const.stepsTurm, const.delayTurm, const.richtungTurmDrehtRechts)
    cleanup(pins_turm)
    
 

