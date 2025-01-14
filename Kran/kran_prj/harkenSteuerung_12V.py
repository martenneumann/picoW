########################################################################################################
# Dieses Modul dient der Steuerung des Elektromagnetens welcher als Harken an dem Kran dient
# Der Elektromagnet soll mittels der H-Bruecke L298N mit 12 Volt betiben werden
#
# @Status : Getestet Funktioniert
#
########################################################################################################

########################################################################################################
# Importiere von Module
########################################################################################################
import utime
import logger	# Loggingmodul auf den Terminal der Thonny IDE
import const	# Fuer Pinnbelegungen und globale Variablen
from machine import Pin

########################################################################################################
# Hier werden die GPIO Pins definiert
########################################################################################################
pin_HarkenIn1 = Pin(const.gpio_hBrueckeIn1, Pin.OUT)
pin_HarkenIn2 = Pin(const.gpio_hBrueckeIn2, Pin.OUT)

########################################################################################################
# Setze die Pins an der H-Bruecke abhaegig von den Aufrufparameter
# @input : in1 = 0 oder 1 um GPIO zu steuern
# @input : in2 = 0 oder 1 um GPIO zu steuern
########################################################################################################
def setzePinIn1In2_L298N(in1, in2):
    pin_HarkenIn1.value(in1)
    pin_HarkenIn2.value(in2)

########################################################################################################
# Schaltet den Harken an und logged dies weg
########################################################################################################
def harkenAn():
    setzePinIn1In2_L298N(0, 1)
    logger.log("Harken Einschalten", "Harken")
    
########################################################################################################
# Schaltet den Harken aus und logged dies Weg
# Vor dem Ausschalten wird der Elektromagnet kurz umgepolt. Diese Zeit reicht nicht, dass Gegenstaende
# vom Magneten fallen. Die hoffnung ist die, so das Metall am Harken etwas zu entmagnetisieren.
# Es hat sich gezeigt, dass gegenstände sonst "kleben" bleiben
########################################################################################################
def harkenAus():
    setzePinIn1In2_L298N(1, 0)
    utime.sleep_ms(2)
    setzePinIn1In2_L298N(0, 0)
    logger.log("Harken Ausschalten", "Harken")

