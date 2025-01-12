import hbrueckenSteuerung
import sensorUeberwachung
import const
import utime

if __name__ == "__main__":

    while True:
        print("---------------------------------------------")
        print("1 Zug zum ersten Haltepunkt fahre (erstmals reinfahren)")
        print("2 Zug zum zweiten Haltepunkt fahre (zweites mal entladen)")
        print("3 Zug Rausfahren")
        eingabe = input("Eingabe : ")
        print("---------------------------------------------")
        
                
        if eingabe == "1":
            sensorUeberwachung.sensorUberwachungStarten()
            hbrueckenSteuerung.fahreZugRein(const.minZugSpeed, const.abbruchzeitZugErsterHaltepunkt)
            sensorUeberwachung.sensorUberwachungStoppen()
        elif eingabe == "2":
            sensorUeberwachung.sensorUberwachungStarten()
            hbrueckenSteuerung.fahreZugRein(const.minZugSpeed, const.abbruchzeitZugZweiterHaltepunkt)
            sensorUeberwachung.sensorUberwachungStoppen()
        elif eingabe == "3":
            sensorUeberwachung.sensorUberwachungStarten()
            hbrueckenSteuerung.fahreZugRaus(const.minZugSpeed, const.abbruchzeitZugVerlaesstBereich)
            sensorUeberwachung.sensorUberwachungStoppen()
        else :
            print("Fehleingabe")
            
            
