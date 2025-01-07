import windenMotor



if __name__ == "__main__":
    while True:
        print("---------------------------------------------")
        print("1 Harken runter Fahren")
        print("2 Harken hoch Fahren")
        eingabe = input("Eingabe : ")
        print("---------------------------------------------")
        
        if eingabe == "1":
            windenMotor.fahreHarkenRunter()
        elif eingabe == "2":    
            windenMotor.fahreHarkenHoch()
        else :
            print("Fehleingabe")        

    

