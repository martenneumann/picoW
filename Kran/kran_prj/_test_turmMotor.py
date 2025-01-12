#Getestet
import turmMotor
import const
import utime

if __name__ == "__main__":
    while True:
        print("---------------------------------------------")        
        print("1 fuer Turm position 1 (0 Grad)")
        print("2 fuer Turm position 2 (90 Grad)")
        print("3 fuer Turm position 3 (180 Grad)")
        print("4 fuer Turm Motor ausschalten # Position 1 einnehmen")        
        eingabe = input("Eingabe : ")
        print("---------------------------------------------")        
        
        if eingabe == "1":
            turmMotor.fahreTurmInPosition1(const.speed_schrittweite_Turmmotor)
        elif eingabe == "2":
            turmMotor.fahreTurmInPosition2(const.speed_schrittweite_Turmmotor)
        elif eingabe == "3":
            turmMotor.fahreTurmInPosition3(const.speed_schrittweite_Turmmotor)
        elif eingabe == "4":             
            turmMotor.turmMotorAusschalten(const.speed_schrittweite_Turmmotor)
        else :
            print("Fehleingabe")        

    

