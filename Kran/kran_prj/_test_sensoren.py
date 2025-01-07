import sensorUeberwachung
import utime

if __name__ == "__main__":   

    print("Achtung: Testprogramm könnte Thread nicht beenden. Pico abziehen und wieder anschließen nach beendigung")
    while True :
        print("---------------------------------------------")
        print("1 Nur zusstandsänderungen von Lichtschranke + Reeed Schalter (Normaler modi)")
        print("2 Lichtschranke durchgängig Tracen")
        print("3 Reed Schalter durchgängig Tracen")
        eingabe = input("Eingabe : ")
        print("---------------------------------------------")

        if eingabe == "1":
            print("Achtung: Testprogramm könnte Thread nicht beenden. Pico abziehen und wieder anschließen nach beendigung")
            sensorUeberwachung.sensorUberwachungStarten()
            while True : continue
        elif eingabe == "2":
            while True :
                sensorUeberwachung.lichtschrankeUeberwachen()
                print("Lichtsschranke zug Erkannt (geschlossen)" if sensorUeberwachung.lSchranke_ZugErkannt == 1 else "Lichtsschranke kein Zug erkannt (offen)")
                utime.sleep_ms(500)                
        elif eingabe == "3":
            while True :
                sensorUeberwachung.reedSchalterUeberwachen()
                print("Reedschalter zug Erkannt (geschlossen)" if sensorUeberwachung.reedSchalter_ZugErkannt == 1 else "Reedschalter kein Zug erkannt (offen)")
                utime.sleep_ms(500)
        else :
            print("Fehleingabe") 