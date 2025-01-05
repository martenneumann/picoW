import sensorUeberwachung

if __name__ == "__main__":   
    sensorUeberwachung.sensorUberwachungStarten()
    print("Achtung: Testprogramm beendet Thread nicht. Pico abziehen und wieder anschließen nach beendigung")
    while True : continue
