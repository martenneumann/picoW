import kranMotoren
import const
import logger
import utime

if __name__ == "__main__":
    while True:
        eingabe = input("Gebe 1 fuer Harken Runter; 0 (Null) fuer Harken Hoch : ")
        steps   = int(input("Gebe eine strecke fue das Seil an (zb. 200) : "))
        speed   = float(input("Gebe eine geschwindigkeit an (0.001 max speed) : "))
        if eingabe == "1":
            kranMotoren.fahreHarkenRunter(steps, speed)
        elif eingabe == "0":    
            kranMotoren.fahreHarkenHoch(steps, speed)
        else :
            print("Fehleingabe")        

