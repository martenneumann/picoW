import turmMotor
import const
import utime

if __name__ == "__main__":
    while True:
        print("---------------------------------------------")        
        print("1 fuer Turm position 1 (0 Grad)")
        print("2 fuer Turm position 2 (90 Grad)")
        print("3 fuer Turm position 3 (180 Grad)")
        print("4 fuer Turm Motor ausschalten - Position 1 einnehmen")        
        eingabe = input("Eingabe 1 von 2: ")
        print("Gebe eine geschwindigkeit ein (speed_schrittweite_Turmmotor zb. 10000)")  
        speed   = int(input("Eingabe 2 von 2 : "))
        print("---------------------------------------------")        
        
        if eingabe == "1":
            turmMotor.fahreTurmInPosition1(speed)
        elif eingabe == "2":
            turmMotor.fahreTurmInPosition2(speed)
        elif eingabe == "3":
            turmMotor.fahreTurmInPosition3(speed)
        elif eingabe == "4":             
            turmMotor.turmMotorAusschalten(speed)
        else :
            print("Fehleingabe")        
   


  

