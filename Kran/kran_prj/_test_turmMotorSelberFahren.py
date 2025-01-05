import kranMotoren
import const
import logger
import utime

if __name__ == "__main__":
    while True:
        eingabe = input("Gebe 1 fuer Turm rechts rotieren 0 (Null) Turm links rotieren : ")
        steps   = int(input("Gebe eine strecke fue das Seil an (zb. 200) : "))
        speed   = float(input("Gebe eine geschwindigkeit an (0.001 max speed) : "))
        if eingabe == "1":
            kranMotoren.rotiereTurmRecht(steps, speed)
        elif eingabe == "0":    
            kranMotoren.rotiereTurmLinks(steps, speed)
        else :
            print("Fehleingabe")        
  

