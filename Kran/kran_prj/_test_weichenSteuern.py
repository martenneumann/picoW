import weichenSteuerung
import utime

if __name__ == "__main__":
    while True:
        print("---------------------------------------------")        
        print("1 Weiche oeffnen")
        print("2 Weiche schliessen")     
        eingabe = input("Eingabe : ")
        print("---------------------------------------------")
        
        if eingabe == "1":
            weichenSteuerung.weicheOeffnen()
        elif eingabe == "2":    
            weichenSteuerung.weicheSchliessen()
        else :
            print("Fehleingabe")
    