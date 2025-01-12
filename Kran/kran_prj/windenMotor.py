# Getestet Funktioniert
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

# Sequenz für den ULN2003 (Halbschrittmodus)
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
# 
########################################################################################################
def set_step(sequence):
    for pin, value in zip(pins_winde, sequence):
        pin.value(value)

########################################################################################################
# 
########################################################################################################
def step_motor(steps, delay, direction):
    for _ in range(steps):
        for step in (MOTOR_MAGNET_SEQ if direction == 1 else reversed(MOTOR_MAGNET_SEQ)):
            set_step(step)
            time.sleep(delay)      

########################################################################################################
# 
########################################################################################################
def cleanup():
    set_step([0, 0, 0, 0])

########################################################################################################
# 
########################################################################################################
def fahreHarkenHoch(steps = const.stepsHarken, speed = const.delayHarken) :
    logger.log("Harken hoch fahren", "HARKEN_MOTOR")
    step_motor(steps, speed, const.richtungHarkenHoch)
    cleanup()

########################################################################################################
# 
########################################################################################################
def fahreHarkenRunter(steps = const.stepsHarken, speed = const.delayHarken) :
    logger.log("Harken runter fahren", "HARKEN_MOTOR")
    step_motor(steps, speed, const.richtungHarkenRunter)
    cleanup()
    


    
 

