########################################################################################################
# In dieser Datei sollen alle Globalen Variablen definiert werden. Dies dient dazu z.B Pin definitionen
# nicht über den gesamten Quelltext zu verteilen sonder zu Zentralisieren. Hierdurch koennen fehler wie
# doppeltbelegungen von Pins leichter gefunden werden. Durch Testen einzelner Module würde diese Art von
# fehler wahrscheinlich garnicht entdeckt werden können.
#
# Eine weiterer vorteil ist, dass bei der Feinjustierung des Krans (z.B. Geschwindigkeiten oder Warte-
# zeiten) nurnoch diese Zentrale Datei editiert und hochgeladen werden muss
########################################################################################################    

########################################################################################################
# GPIO Pin belegung fuer die H-Bruecke L298N. In1 und 2 dienen für Out 1 und 2 wo der Elektromagnet
# Angeschlossen ist In 3 und 4 sowie der ENB Pin fuer die elektrifizierung der Gleise Out 3 und 4.
# Der ENB Pin kann den Ausgang OUT 3 - 4 komplett deaktivieren eignet sich d.h. für PWM
######################################################################################################## 
gpio_hBrueckeENB			= 20
gpio_hBrueckeIn4			= 19
gpio_hBrueckeIn3			= 18
gpio_hBrueckeIn2			= 17
gpio_hBrueckeIn1			= 16

########################################################################################################
# GPIO Pin belegung fuer Llichtschranke und Reet Schalter.
# ACHTUNG: Lichtschrankenausgabe ist "invertiert" zum erwartungswert. Kabelbruchsicher
######################################################################################################## 
gpio_LichtschrankeLesen		= 15	# Pin um Lichtschranke zu lesen
gpio_ReetSchalterLesen		= 14	# Pin um Reed Schlater zu lesen

########################################################################################################
# GPIO Pin fuer den Motor Treiber ULN2003 um den Windenmotor zu steuern.
# Der Windenmotor ist vom Typ 28BY-48 und hat 4 seperat steuerbare Wicklungen
######################################################################################################## 
gpio_windenMotorIn1			= 13
gpio_windenMotorIn2			= 12
gpio_windenMotorIn3			= 11
gpio_windenMotorIn4			= 10

########################################################################################################
# GPIO Pin fuer die Servomotoren SG90
# ACHTUNG : Ist deren Poti nicht in Grundstellung rotieren sie bei initialisierung sehr schnell
######################################################################################################## 
gpio_weichenMotor			= 5
gpio_turmMotor				= 4

########################################################################################################
# GPIO Pin um Elektromagnet zu steuern
# ACHTUNG : Aufgrund von Designaenderungen nun nicht mehr ueber GPIO 3
######################################################################################################## 
#gpio_harkenAktivieren		= 3		# Pin um den Elektromagneten einzuschalten

########################################################################################################
# GPIO Pins fuer die Stellwerk Kommunikation. Fuer details siehe Doku
# gpio_stellwReq : Pin schreibt anfrage ans Stellwerk.
# gpio_stellwAck : Fallende flanke an diesem Pin bedeutet OK
# gpio_simulationsStellwReq : Mit diesem Pin soll das Stellwerk Simuliert werden können
######################################################################################################## 
gpio_simulationsStellwReq	= 2		
gpio_stellwReq				= 1		
gpio_stellwAck				= 0		# Pin liesst Stellwerk antwort. Fallende Flanke Ok. Ohne Stellwerk mit GPIO 1 verbinden


########################################################################################################
# GLOBALEN
########################################################################################################

########################################################################################################
# Zeit in der die beiden Sensoren (Reedsschalter und Lichtschranke) innerhalb ihres eigenen Threads
# Zyklisch abgefragt werden sollen
########################################################################################################
sensorUeberwachungLoopSleepTimeMs = 1

########################################################################################################
# Windenmotor
########################################################################################################
stepsHarken 					= 1500				# Hierüber lässt sich einstellen wie viel Faden von der Winde abgewickelt werden soll. Je größer desto mehr.
stepsHarkenOffset				= 150               # Hier lässt sich die einstellen wie viel mehr Faden gegeben werden muss um den Boden zu erreichen. Differnez Boden zu Wagon
delayHarken 					= float(0.002)		# Geschwindigkeit mit der der Faden abgerollt werden soll. 0.001 max geschwindigkeit
richtungHarkenHoch				= 1					# Winde wickelt Faden auf
richtungHarkenRunter			= -1				# Winde wickelt Faden ab

########################################################################################################
# Turmmotor alt
########################################################################################################
#stepsTurn180Grad				= 260				# Hierüber lässt sich einstellen wie weit der Turm gedreht werden soll. 220 ca 180 Grad.
#delayTurn						= float(0.005)		# Geschwindigkeit mit der der Turm rotieren soll. 0.001 max geschwindigkeit
#speedTurmmotor					= 0.02				# Geschwindigkeit mit der der Turm rotieren soll. Besser nicht ueber 0.02

########################################################################################################
# H-Bruecken schaltrichtung
########################################################################################################
gleisstromZugRein				= 1					# Wie rum sollen die Gleise unter Strom. 1 == Zug Rein, 0 == Zug Raus
gelisstromZugRaus				= 0					# Wie rum sollen die Gleise unter Strom. 1 == Zug Rein, 0 == Zug Raus

########################################################################################################
# Weiche
# Die Werte fuer den PWM Winkel kommen aus  der Mail "micropython Programme" vom 25.09.2024 - 08:20
########################################################################################################
weichenMotorTraegerFrq			= 50				# Taeger Frequenz fuer Weichenmotor
endlageWeicheAuf				= 1500000			# PWM duty time fuer Weiche auf; Gibt Winkel an
endlageWeicheZu					= 1300000			# PWM duty time fuer Weiche zu; Gibt Winkel an

########################################################################################################
# Turmmotor neu
########################################################################################################
turmMotorGrad000				= 500000			# PWM duty fuer den Winkel des Turmmotors
turmMotorGrad090				= 1500000			# PWM duty fuer den Winkel des Turmmotors
turmMotorGrad180				= 2500000			# PWM duty fuer den Winkel des Turmmotors
speed_schrittweite_Turmmotor	= 5000				# Drehwinkel des Turms innerhalb eines Drehschrittes
verzoegerungTurmMotor			= 0.02				# Verlangsamt das drehen des Turmmotors in ns zwischen einem Drehschritt
richtungTurmDrehtRechts			= 1					# Turm dreht sich nach Rechts
richtungTurmDrehtLinks			= -1				# Turm dreht sich nach Links

########################################################################################################
# Stellwerk Simulation
########################################################################################################
stellwSimulationTasteSteigendeFlanke = "s" # Drücken dieser Taste erzeugt eine steigende Flanke
stellwSimulationTasteFallendeFlanke	 = "f" # Drücken dieser Taste erzeugt eine fallende Flanke

########################################################################################################
# Zug fahren
########################################################################################################
minZugSpeed						= 45				# Min duty time fuer schwarzen zug zum bewegen. In Prozent.
                                                    # Wahrscheinlich zwischen 40% und 45% NOCH ZU TESTEN!!!
abbruchsZeitInMs_ZugReinfahren 	= 3000				# In Ms. Nach dieser Zeit schaltet die H-Brücke ab. Damit Zug nicht zuweit fährt.
                                                    # Kann auch genutzt werden,  wenn Reed kontakt nicht ordentlich greift. Dann kann
                                                    # versucht werden über diesen Parameter den Zug unter den Kran zu stellen.
                                                    # Zeit in Millisekunden. WERT MUSS NOCH DURCH TESTEN RAUSGEFUNDEN WERDEN

abbruchsZeitInMs_ZugRausfahren  = 30000				# In Ms. Nach dieser Zeit schaltet die H-Brücke ab. Damit Zug nicht zuweit fährt.
                                                    # Diesmal nur beim Rausfahren.
                                           



