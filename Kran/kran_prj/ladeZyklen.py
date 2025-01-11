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
    windenMotor.fahreHarkenRunter_Wagon()
    utime.sleep(2)
    harkenSteuerung_12V.harkenAn()
    utime.sleep(2)
    windenMotor.fahreHarkenHoch_Wagon()
    utime.sleep(2)
    turmMotor.fahreTurmInPosition3(const.speed_schrittweite_Turmmotor)
    utime.sleep(2)        
    windenMotor.fahreHarkenRunter_Wagon()
    utime.sleep(2)
    harkenSteuerung_12V.harkenAus()
    utime.sleep(2)
    windenMotor.fahreHarkenHoch_Wagon()
    utime.sleep(2)
    turmMotor.fahreTurmInPosition1(const.speed_schrittweite_Turmmotor)
    logger.log("ENDE Entladezyklus", "INFO")      
