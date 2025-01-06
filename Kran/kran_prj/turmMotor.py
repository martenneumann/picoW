# Bibliotheken laden
from machine import Pin, PWM
from time import sleep
import const

# Funktionen für die Servo-Steuerung
def set_angle(pwm, angle_ns):
    pwm.duty_ns(angle_ns)
    sleep(const.speedTurmmotor)  # Kurze Verzögerung zwischen den Schritten

def move_smooth(pwm, start_ns, end_ns, step_ns):
    if start_ns < end_ns:
        for duty in range(start_ns, end_ns + 1, step_ns):
            set_angle(pwm, duty)
    else:
        for duty in range(start_ns, end_ns - 1, -step_ns):
            set_angle(pwm, duty)

# Servo-PWM initialisieren
pwm = PWM(Pin(const.gpio_turmMotor))
pwm.freq(50)  # Typische Frequenz für Servos ist 50 Hz

# Winkel in Nanosekunden (ns)
grad000 = 500000
grad090 = 1500000
grad180 = 2500000

# Schrittweite (z. B. 10000 ns pro Schritt)
step_ns = 10000

# Start bei 0 Grad und langsam zur Mitte (90 Grad) bewegen
print('Position: Mitte (90 Grad)')
move_smooth(pwm, grad000, grad090, step_ns)
sleep(1)

print('Position: Ganz Links (0 Grad)')
move_smooth(pwm, grad090, grad000, step_ns)
sleep(1)

print('Position: Mitte (90 Grad)')
move_smooth(pwm, grad000, grad090, step_ns)
sleep(1)

print('Position: Ganz Rechts (180 Grad)')
move_smooth(pwm, grad090, grad180, step_ns)
sleep(1)

print('Position: Mitte (90 Grad)')
move_smooth(pwm, grad180, grad090, step_ns)
sleep(1)

pwm.deinit()
print('Ende')

