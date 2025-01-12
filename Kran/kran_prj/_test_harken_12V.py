# Getestet Funktioniert
import harkenSteuerung_12V
import utime

if __name__ == "__main__":
    while True:
        print("---------------------------------------------")
        print("1 fuer Harken Einschalten")
        print("2 fuer Harken Ausschalten")
        eingabe = input("Eingabe : ")
        print("---------------------------------------------")
        
        if eingabe == "1":
            harkenSteuerung_12V.harkenAn()
        elif eingabe == "2":    
            harkenSteuerung_12V.harkenAus()
        else :
            print("Fehleingabe")        

    

