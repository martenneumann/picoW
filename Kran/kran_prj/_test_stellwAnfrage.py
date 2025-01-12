# FUNKTIONIERT
import stellwAnfrage
import utime

if __name__ == "__main__":
    while True:
        print("---------------------------------------------")
        print("Um eine antwort vom Stellwerk zu simulieren s druecken == Steigende flanke, dann")
        print("dann f druecken == Fallende flanke. Damit wurde ein ACK ausgelöst")
        print("1 Weiche offnen Anfragen und auf Antwort warten")
        print("2 Weiche schliessn Anfragen und auf Antwort warten")
        eingabe = input("Eingabe : ")
        print("---------------------------------------------")
        

        
        if eingabe == "1":
            stellwAnfrage.weichenOeffnenErlaubtAnfragenAntwortAbwarten()
        elif eingabe == "2":
            stellwAnfrage.weichenSchliessenErlaubtAnfragenAntwortAbwarten()         
            
        else :
            print("Fehleingabe")        
