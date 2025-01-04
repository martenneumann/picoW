import motorenSteuern
import utime

if __name__ == "__main__":
            motorenSteuern.weicheOeffnen()
            utime.sleep(1)
            motorenSteuern.weicheSchliessen()
            utime.sleep(1)
    