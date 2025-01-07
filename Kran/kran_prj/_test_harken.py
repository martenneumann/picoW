import harkenSteuerung
import utime

if __name__ == "__main__":
    while True:
        print("---------------------------------------------")
        print("1 fuer Harken Einschalten")
        print("2 fuer Harken Ausschalten")
        eingabe = input("Eingabe : ")
        print("---------------------------------------------")
        
        if eingabe == "1":
            harkenSteuerung.harkenAn()
        elif eingabe == "2":    
            harkenSteuerung.harkenAus()
        else :
            print("Fehleingabe")        

    
