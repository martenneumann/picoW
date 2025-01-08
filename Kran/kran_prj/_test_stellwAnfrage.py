import stellwAnfrage
import const
import utime

if __name__ == "__main__":
    while True:
        print("---------------------------------------------")
        print("Um eine antwort vom Stellwerk zu simulieren x druecken == Steigende flanke")
        print("Zweites mal x drücken == fallende Flanke")          
        print("1 Weiche offnen Anfragen und auf Antwort warten")
        print("2 Weiche schliessn Anfragen und auf Antwort warten")
        eingabe = input("Eingabe : ")
        print("---------------------------------------------")
        

        
        if eingabe == "1":
            weichenOeffnenErlaubtAnfragenAntwortAbwarten()
        elif eingabe == "2":
            weichenSchliessenErlaubtAnfragenAntwortAbwarten()         
            
        else :
            print("Fehleingabe")        
