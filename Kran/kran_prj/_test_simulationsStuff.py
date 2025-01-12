# FUNKTIONIERT
import simulationsStuff
import utime

if __name__ == "__main__":
    while True:
        print("---------------------------------------------")        
        print("1 Um Tasteneingabe im bib 'Simulations Stuff' zu testen")        
        eingabe = input("Eingabe : ")
        print("---------------------------------------------")        
        
        if eingabe == "1":
            while True :
                vonTastatur = simulationsStuff.pruefeAufTestaturEingabe()
                print(f"Es wurde eingegeben : {vonTastatur}")
                if vonTastatur == "x" : print ("Eingabe von x erkannt")
                utime.sleep(1)
