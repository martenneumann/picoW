import weichenSteuerung
import utime

if __name__ == "__main__":
    while True:
        eingabe = input("Gebe 1 fuer Oeffnen; 0 (Null) fuer Schliessen : ")
        if eingabe == "0":
            weichenSteuerung.weicheOeffnen()
        elif eingabe == "1":    
            weichenSteuerung.weicheSchliessen()
        else :
            print("Fehleingabe")
    