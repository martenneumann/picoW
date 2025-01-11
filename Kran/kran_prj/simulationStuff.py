import sys
import select
import logger

########################################################################################################
# 
########################################################################################################
def pruefeAufTestaturEingabe():
    if select.select([sys.stdin], [], [], 0)[0]:
        eingabe = sys.stdin.readline().strip()
        logger.log(f"ACHTUNG : Es gab eine Tastatureingabe : '{eingabe}'", "SIMULATION")
        return eingabe
    return None
