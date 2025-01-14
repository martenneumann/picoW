########################################################################################################
# Dieses Modul ist ein Hilfsmodul und hat seinerseits kein Interface zu einem Aktor oder Sensor.
# Die Aufgabe dieses Moduls ist es den kompletten Bewegungsablaufs des Krans beim Be- und Entladen
# abzubilden.
# Die nutzung dieses Moduls schafft übersichtlichkeit in der Main und ermöglicht es ueber sein Test-
# programm den Kran seperiert von der Streckenseite zu Testen
#
# @Status : Getestet Funktioniert
#
########################################################################################################

import logger	# Loggingmodul auf den Terminal der Thonny IDE
import const	# Fuer Pinnbelegungen und globale Variablen
import utime
import turmMotor 
import windenMotor
import harkenSteuerung_12V

########################################################################################################
# Bildet alle notwendigen schritte des Krans für einen Entladezykus ab
########################################################################################################    
def fahreEntladeZyclus():
    logger.log("START Entladezyklus", "INFO")
    harkenNimmtGegenstandAuf()
    turmMotor.fahreTurmInPosition3(const.speed_schrittweite_Turmmotor)
    utime.sleep(2)
    harkenLaesstGegenstandAb()
    turmMotor.fahreTurmInPosition1(const.speed_schrittweite_Turmmotor)
    utime.sleep(2)
    logger.log("ENDE Entladezyklus", "INFO")
    
########################################################################################################
# Bildet alle notwendigen schritte des Krans für einen Ent- und Beladezyklus ab
########################################################################################################    
def fahreEntladeUndBeladeZyclus() :
    logger.log("START Entlade und wieder Belade zyklus", "INFO")
    harkenNimmtGegenstandAuf()
    turmMotor.fahreTurmInPosition3(const.speed_schrittweite_Turmmotor)
    utime.sleep(2)
    harkenLaesstGegenstandAb()
    turmMotor.fahreTurmInPosition2(const.speed_schrittweite_Turmmotor)
    utime.sleep(2)
    harkenNimmtGegenstandAuf()
    turmMotor.fahreTurmInPosition1(const.speed_schrittweite_Turmmotor)
    utime.sleep(2)
    harkenLaesstGegenstandAb()
    logger.log("ENDE Entlade und wieder Belade zyklus", "INFO")

    
########################################################################################################
# Bildet kompletten Zyklus ab um mit den Harken aus der Position
# "Harken oben" , "Harken leer" einen Gegenstand aufzunehmen
########################################################################################################
def harkenNimmtGegenstandAuf() :
    windenMotor.fahreHarkenRunter()
    utime.sleep(2)
    harkenSteuerung_12V.harkenAn()
    utime.sleep(2)
    windenMotor.fahreHarkenHoch()
    utime.sleep(2)
    
########################################################################################################
# Bildet kompletten Zyklus ab um mit den Harken aus der Position
# "Harken oben" , "Harken mit Gegenstand" den geladenen Gegenstand Abzusetzen
########################################################################################################
def harkenLaesstGegenstandAb() :    
    windenMotor.fahreHarkenRunter()
    utime.sleep(2)
    harkenSteuerung_12V.harkenAus()
    utime.sleep(2)
    windenMotor.fahreHarkenHoch()    