import weichenSteuerung
import utime

if __name__ == "__main__":
    while True:
        eingabe = input("Gebe 1 fuer Oeffnen; 0 (Null) fuer Schliessen : ")
        if eingabe == "1":
            weichenSteuerung.weicheOeffnen()
        elif eingabe == "0":    
            weichenSteuerung.weicheSchliessen()
        else :
            print("Fehleingabe")
    