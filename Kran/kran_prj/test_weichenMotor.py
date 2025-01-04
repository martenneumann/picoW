import weichenSteuerung
import utime

if __name__ == "__main__":
    while True:
        richtung = input("Gebe O fuer Oeffnen oder S fuer Schliessen ein : ")
        if richtung == "O":
            weichenSteuerung.weicheOeffnen()
        elif richtung == "S":    
            weichenSteuerung.weicheSchliessen()
        else :
            print("Fehleingabe")
    