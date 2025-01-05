import kranMotoren
import utime

if __name__ == "__main__":
    while True:
        eingabe = input("Gebe 1 fuer Harken Runter; 0 (Null) fuer Harken Hoch : ")
        if eingabe == "1":
            kranMotoren.fahreHarkenRunter()
        elif eingabe == "0":    
            kranMotoren.fahreHarkenHoch()
        else :
            print("Fehleingabe")        

    

