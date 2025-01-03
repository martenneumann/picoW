import utime

# Initialisiere den Startzeitpunkt
START_TIME = utime.ticks_ms()

########################################################################################################
#    Gibt die Zeit seit dem Start des Programms in Sekunden zurück.
########################################################################################################
def _get_timestamp():
    elapsed_time = utime.ticks_diff(utime.ticks_ms(), START_TIME) // 1000
    minutes = elapsed_time // 60
    seconds = elapsed_time % 60
    return f"{minutes:02}:{seconds:02}"

########################################################################################################
#    Loggt eine Nachricht mit einem relativen Zeitstempel und Log-Level.
#    
#    Args:
#        message (str): Die Nachricht, die geloggt werden soll.
#        level (str): Das Log-Level (z.B. "INFO", "ERROR"). Standard ist "INFO".
########################################################################################################
def log(message, level="INFO"):
    timestamp = _get_timestamp()
    print(f"[{timestamp}] [{level}] {message}")


# Loggt alle Sensoren aus der übergebenen Klasse
def log_all_sensors(sensor_class):
    for sensor in dir(sensor_class):
        # Nur die Konstanten (die "Sensoren") berücksichtigen
        if not sensor.startswith('__'):
            sensor_info = getattr(sensor_class, sensor)
            log(f"Sensor {sensor_info[0]} mit Pin {sensor_info[1]} aktiv.", "INFO")