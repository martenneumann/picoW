import zugSteuerung
import sensorUeberwachung
import const


if __name__ == "__main__":

    while True:
        print("---------------------------------------------")
        print("1 Zug Reinfahre ")
        print("2 Zug Rausfahren")
        print("3 Stopp Kommando")        
        eingabe = input("Eingabe : ")
        print("---------------------------------------------")
        
                
        if eingabe == "1":
            sensorUeberwachung.sensorUberwachungStarten()
            zugSteuerung.fahreZugRein(const.minZugSpeed, const.abbruchsZeitInMs_ZugReinfahren)
            sensorUeberwachung.sensorUberwachungStoppen()
        elif eingabe == "2":
            sensorUeberwachung.sensorUberwachungStarten()
            zugSteuerung.fahreZugRaus(const.minZugSpeed, const.abbruchsZeitInMs_ZugReinfahren)
            sensorUeberwachung.sensorUberwachungStoppen()
        elif eingabe == "3":            
            zugSteuerung.stoppeZug()
        else :
            print("Fehleingabe")
            
            
