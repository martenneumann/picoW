# GETESTET
import logger

if __name__ == "__main__":

    while True:
        print("---------------------------------------------")
        print("Gebe einen Text ein, der Gelogged werden soll")
        text = input("Eingabe 1 von 2: ")
        print("Gebe einen Modul ein (z.b. TURM, HARKEN, usw.) welches loggen soll")
        modul = input("Eingabe 2 von 2: ")        
        print("---------------------------------------------")
        logger.log(f"{text}", f"{modul}")