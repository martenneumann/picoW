import windenMotor



if __name__ == "__main__":
    while True:
        print("---------------------------------------------")
        print("1 Harken runter Fahren : In den Wagon")
        print("2 Harken hoch Fahren   : Aus dem Wagon")
        print("3 Harken runter Fahren : Auf den Ladeplatz")
        print("4 Harken hoch Fahren   : Von dem Ladeplatz")        
        eingabe = input("Eingabe : ")
        print("---------------------------------------------")
        
        if eingabe == "1":
            windenMotor.fahreHarkenRunter_Wagon()
        elif eingabe == "2":    
            windenMotor.fahreHarkenHoch_Wagon()
        elif eingabe == "3":
            windenMotor.fahreHarkenHoch_Ladeplatz()
        elif eingabe == "4":    
            windenMotor.fahreHarkenRunter_Ladeplatz()            
        else :
            print("Fehleingabe")        
