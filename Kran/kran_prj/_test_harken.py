import harkenSteuerung
import utime

if __name__ == "__main__":
    while True:
        richtung = input("Gebe 1 fuer Harken EINSCHALTEN 0 (Null) fuer Harken AUSSCHALTEN : ")
        if richtung == "1":
            harkenSteuerung.harkenAn()
        elif richtung == "0":    
            harkenSteuerung.harkenAus()
        else :
            print("Fehleingabe")        

    
