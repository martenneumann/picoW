from machine import Pin
import logger
import time


steps 	= 1500
delay 	= float(0.002)


# GPIO-Pin-Definitionen
pins = [
    Pin(13, Pin.OUT),  # IN1
    Pin(12, Pin.OUT),  # IN2
    Pin(11, Pin.OUT),  # IN3
    Pin(10, Pin.OUT),  # IN4
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

def set_step(sequence):
    """Setzt die Pins gemäß der übergebenen Sequenz."""
    for pin, value in zip(pins, sequence):
        pin.value(value)

def step_motor(steps, delay, direction=1):
    """
    Bewegt den Motor um eine bestimmte Anzahl von Schritten.

    :param steps: Anzahl der Schritte.
    :param delay: Verzögerung zwischen den Schritten in Sekunden.
    :param direction: Richtung des Motors (1 = vorwärts, -1 = rückwärts).
    """
    for _ in range(steps):
        for step in (SEQUENCE if direction == 1 else reversed(SEQUENCE)):
            set_step(step)
            time.sleep(delay)

def cleanup():
    """Setzt alle Pins auf 0, um den Motor zu stoppen."""
    set_step([0, 0, 0, 0])

def fahreHarkenHoch() :
    logger.log("Harken runter fahren", "H_MOTOR")
    step_motor(steps, delay, 1)
    cleanup()
    
def fahreHarkenRunter() :
    logger.log("Harken hoch fahren", "H_MOTOR")
    step_motor(steps, delay, -1)
    cleanup()

