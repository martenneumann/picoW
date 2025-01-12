import logger
import const
import utime
import turmMotor
import windenMotor
import harkenSteuerung_12V

########################################################################################################
# 
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
# 
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
# 
########################################################################################################
def harkenNimmtGegenstandAuf() :
    windenMotor.fahreHarkenRunter()
    utime.sleep(2)
    harkenSteuerung_12V.harkenAn()
    utime.sleep(2)
    windenMotor.fahreHarkenHoch()
    utime.sleep(2)
    
########################################################################################################
# 
########################################################################################################
def harkenLaesstGegenstandAb() :    
    windenMotor.fahreHarkenRunter()
    utime.sleep(2)
    harkenSteuerung_12V.harkenAus()
    utime.sleep(2)
    windenMotor.fahreHarkenHoch()    