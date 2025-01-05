import logger
import const
import utime
import kranMotoren
import harkenSteuerung

########################################################################################################
# 
########################################################################################################    
def fahreEntladeZyclus():
    logger.log("START Entladezyklus", "INFO")
    kranMotoren.fahreHarkenRunter()
    utime.sleep(2)
    harkenSteuerung.harkenAn()
    utime.sleep(2)
    kranMotoren.fahreHarkenHoch()
    utime.sleep(2)
    kranMotoren.rotiereTurmRecht()
    utime.sleep(2)        
    kranMotoren.fahreHarkenRunter()
    utime.sleep(2)
    harkenSteuerung.harkenAus()
    utime.sleep(2)
    kranMotoren.fahreHarkenHoch()
    utime.sleep(2)
    kranMotoren.rotiereTurmLinks()
    logger.log("ENDE Entladezyklus", "INFO")      
