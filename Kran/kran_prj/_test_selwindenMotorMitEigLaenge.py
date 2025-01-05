import kranMotoren
import const
import logger
import utime

if __name__ == "__main__":
    while True:
        eingabe  = input("Gebe 1 fuer Harken Runter; 0 (Null) fuer Harken Hoch : ")
        schritte = int(input("Gebe die zu fahrenden Schritte ein  : "))
        if eingabe == "1":
            logger.log("Harken hoch fahren", "HARKEN_MOTOR")
            kranMotoren.step_motor(kranMotoren.pins_winde, schritte, const.delayHarken, const.richtungHarkenRunter)
            kranMotoren.cleanup(kranMotoren.pins_winde)
        elif eingabe == "0":    
            logger.log("Harken runter fahren", "HARKEN_MOTOR")
            kranMotoren.step_motor(kranMotoren.pins_winde, schritte, const.delayHarken, const.richtungHarkenHoch)
            kranMotoren.cleanup(kranMotoren.pins_winde)
        else :
            print("Fehleingabe")        

