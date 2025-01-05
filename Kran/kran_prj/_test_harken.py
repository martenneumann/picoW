import harkenSteuerung
import utime

if __name__ == "__main__":
    while True:
        eingabe = input("Gebe 1 fuer Harken EINSCHALTEN 0 (Null) fuer Harken AUSSCHALTEN : ")
        if eingabe == "1":
            harkenSteuerung.harkenAn()
        elif eingabe == "0":    
            harkenSteuerung.harkenAus()
        else :
            print("Fehleingabe")        

    
