import logger
import ladeZyklen

if __name__ == "__main__":
    while True:
        print("---------------------------------------------")
        print("1 Entladezyklus starten")
        print("2 Lade und Endladde Zyklus starten")        
        eingabe = input("Eingabe : ")
        print("---------------------------------------------")
        
        if eingabe == "1" :
            ladeZyklen.fahreEntladeZyclus()
        if eingabe == "2" :
            ladeZyklen.fahreEntladeUndBeladeZyclus()            
        else :
            print("Fehleingabe")       