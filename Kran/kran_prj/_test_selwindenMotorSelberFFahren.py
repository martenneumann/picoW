import windenMotor
import const
import logger
import utime

if __name__ == "__main__":
    while True:
        print("---------------------------------------------")
        print("1 Harken runter Fahren : In den Wagon")
        print("2 Harken hoch Fahren   : Aus dem Wagon")
        print("3 Harken runter Fahren : Auf den Ladeplatz")
        print("4 Harken hoch Fahren   : Von dem Ladeplatz") 
        eingabe = input("Eingabe 1 von 3: ")
        print("Gebe eine strecke fue das Seil an (zb. 200) ")
        steps  	= int(input("Eingabe 2 von 3 : "))
        print("Gebe eine geschwindigkeit an (0.001 max speed)")
        speed   = float(input("Eingabe 3 von 3 : "))
        print("---------------------------------------------")        

        if eingabe == "1":
            windenMotor.fahreHarkenRunter_Wagon(steps, speed)
        elif eingabe == "2":    
            windenMotor.fahreHarkenHoch_Wagon(steps, speed)
        elif eingabe == "3":
            windenMotor.fahreHarkenHoch_Ladeplatz(steps, speed)
        elif eingabe == "4":    
            windenMotor.fahreHarkenRunter_Ladeplatz(steps, speed)            
        else :
            print("Fehleingabe")        
