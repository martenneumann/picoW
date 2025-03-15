# Testskript für getSchallgeschwindigkeit aus steuerung.py in MicroPython

import sys
from steuerung import getSchallgeschwindigkeit

def main():
    tests = {
        0: 331.3,
        20: 343.3,
        -10: 325.3,
        100: 391.3
    }

    for temp, erwartet in tests.items():
        result = getSchallgeschwindigkeit(temp)
        if abs(result - erwartet) < 0.01:
            print("Test bestanden für", temp, ":", result)
        else:
            print("Test fehlgeschlagen für", temp, ": Erwartet", erwartet, ", aber erhalten", result)
            sys.exit(1)

if __name__ == "__main__":
    main()