import turmMotor
import utime

if __name__ == "__main__":
    while True:
        eingabe = input("Gebe 1 fuer Links; 0 (Null) fuer Rechts : ")
        if eingabe == "0":
            turmMotor.weicheOeffnen()
        elif eingabe == "1":    
            turmMotor.weicheSchliessen()
        else :
            print("Fehleingabe")
    
