# Bibliotheken laden
from machine 	import Pin	
from dht 		import DHT11
from utime import sleep_us, ticks_us
import time



##############################################################################################################################################                      
#
##############################################################################################################################################  
trigger 		= Pin(16, Pin.OUT)											# Initialisierung GPIO-Ausgang für Trigger-Signal
echo 			= Pin(17, Pin.IN)
dht11_sensor 	= DHT11(Pin(14, Pin.IN, Pin.PULL_UP))	

##############################################################################################################################################
# https://www.mikrocontroller.net/attachment/218122/HC-SR04_ultraschallmodul_beschreibung_3.pdf
# 1. Das Auslösen eines Messzyklus geschieht durch eine fallende Flanke am Triggereingang (Pin 2 == trigger) für mindestens 10µs.
#    Darufhin wird ein Tonsignal gesendet
# 2. Danach geht der Ausgang (Echo, Pin 3 == echo) sofort auf H-Pegel und das Modul wartet auf den Empfang des Echos.
#    d.h. Checken wir in der ersten While ob der Pin bereits auf H ist, solange holen wir uns immer wieder den Zeitstempel
#    sobald Pin == 1 ist der letzte gespeicherte Zeitstempel die Zeit in der wir das Signal losgeschickt haben 
# 3. Wird dieses detektiert fällt der Ausgang auf L-Pegel 
#    d.h in der zweiten While checken wir ob das Signal angekommen ist == L Pegel. Solange es nicht angekommen ist speichern wir 
#    kontiuirlich den Zeitstempel. Sobald While verlassen ist der letzt gespeicherte Zeitstempel die ankunftszeit des Signals
# 4. Wird kein Echo detektiert verweilt der Ausgang für insgesamt 200ms auf H-Pegel und zeigt so die erfolglose Messung an.
#    In diesem Fall returnen wir den dritten Parameter als false
##############################################################################################################################################                      
def getTonlaufzeit():
    # Erzeuge Flanke
    trigger.low()
    sleep_us(2)
    trigger.high()
    sleep_us(5)
    trigger.low()
    
    # Zeitmessungen
    while echo.value() == 0 : startZeit = ticks_us()
    while echo.value() == 1 : endZeit   = ticks_us()
       
    return time.ticks_diff(endZeit, startZeit)

##############################################################################################################################################
# Returned die aktuelle Temperatur.
# https://sensorkit.joy-it.net/de/sensors/ky-015
##############################################################################################################################################
def getTemperatur():
    dht11_sensor.measure()
    return float(dht11_sensor.temperature())
    
    
    
    