import zugSteuerung
import sensorUeberwachung
import const
import utime

if __name__ == "__main__":

    while True:
        print("---------------------------------------------")        
        print("1 Zug Reinfahren bis Ziel")
        print("2 Zug Rausfahren bis Ziel")     
        eingabe = input("Eingabe 1 von 3: ")
        print("Gebe eine geschwindigkeit in prozent an (min 45 damit schwarzer Zug fährt")  
        speed   = int(input("Eingabe 2 von 3 : "))
        print("Gebe eine abbruchszeit in ms ein, nach der auf jeden fall gestoppt wird")  
        abbruchsZeit   = int(input("Eingabe 3 von 3 : "))        
        print("---------------------------------------------")  
        
                
        if eingabe == "1":
            sensorUeberwachung.sensorUberwachungStarten()
            zzugSteuerung.fahreZugRein(speed, abbruchsZeit)
            sensorUeberwachung.sensorUberwachungStoppen()
        elif eingabe == "2":
            sensorUeberwachung.sensorUberwachungStarten()
            zugSteuerung.fahreZugRaus(speed, abbruchsZeit)
            sensorUeberwachung.sensorUberwachungStoppen()
        else :
            print("Fehleingabe")
            
            

