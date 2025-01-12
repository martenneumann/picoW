#GETESTET
import weichenSteuerung
import utime

if __name__ == "__main__":
    while True:
        print("---------------------------------------------")        
        print("1 Weiche oeffnen")
        print("2 Weiche schliessen")
        print("3 Weiche initial scheissen")          
        eingabe = input("Eingabe : ")
        print("---------------------------------------------")
        
        if eingabe == "1":
            weichenSteuerung.weicheOeffnen()
        elif eingabe == "2":    
            weichenSteuerung.weicheSchliessen()            
        elif eingabe == "3":    
            weichenSteuerung.weicheInitalSchliessen()
        else :
            print("Fehleingabe")
    