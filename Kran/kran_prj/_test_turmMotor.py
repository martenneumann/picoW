import kranMotoren
import utime

if __name__ == "__main__":
    while True:
        eingabe = input("Gebe 1 fuer Turm rechts rotieren 0 (Null) Turm links rotieren : ")
        if eingabe == "1":
            kranMotoren.rotiereTurmRecht()
        elif eingabe == "0":    
            kranMotoren.rotiereTurmLinks()
        else :
            print("Fehleingabe")        

    

