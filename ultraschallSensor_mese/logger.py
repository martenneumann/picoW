import utime
import steuerung

# Initialisiere den Startzeitpunkt, nehme einen Zeitstempel
START_TIME = utime.ticks_ms()

##############################################################################################################################################
# 
##############################################################################################################################################
def dump(dumpForm, durchlauf, messungs_Array, erwartungUndAbweichung_Array, speed) :
    dumpHmi(messungs_Array, erwartungUndAbweichung_Array, speed, durchlauf) if dumpForm == 1 else dumpCsv(messungs_Array, erwartungUndAbweichung_Array, speed, durchlauf)

##############################################################################################################################################
# 
##############################################################################################################################################
def dumpHmi(messungs_Array, erwartungUndAbweichung_Array, speed, durchlauf) :
    zeitStempel = hohleZeitstempel()
    print("**********************************************************************************")
    print(f"Durchlauf = [{durchlauf}] || Zeitstempel = [{zeitStempel}]")
    
    if messungs_Array:
        for i, wert in enumerate(messungs_Array, start=1):
            print(f"Wert {i} = [{wert}] cm")
    else:
        print("Keine Messwerte vorhanden.")
        
    print(f"Erwartungswert = [{erwartungUndAbweichung_Array[-1][0]}] cm")
    print(f"Abweichung = [{erwartungUndAbweichung_Array[-1][1]}] cm")
    
    print(f"Geschwindigkeit {i} = [{speed}] cm/s")
    
##############################################################################################################################################
# 
##############################################################################################################################################
def dumpCsv(messungs_Array, erwartungUndAbweichung_Array, speed, durchlauf) :
    print ("TODO")
    
##############################################################################################################################################
# 
##############################################################################################################################################
def hohleZeitstempel():
    sysZeit = utime.ticks_diff(utime.ticks_ms(), START_TIME) // 1000
    minutes = sysZeit // 60
    seconds = sysZeit % 60
    return f"{minutes:02}:{seconds:02}"