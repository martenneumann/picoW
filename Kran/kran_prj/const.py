from machine import Pin

gpio_hBrueckePwm			= 20	# Pin um den Elektromagneten einzuschalten
gpio_hBrueckeRechts			= 19	# Pin um den Elektromagneten einzuschalten
gpio_hBrueckeLinks			= 18	# Pin um den Elektromagneten einzuschalten
gpio_hBrueckeIn2			= 17	# Pin um den Elektromagneten einzuschalten
gpio_hBrueckeIn1			= 16	# Pin um den Elektromagneten einzuschalten

gpio_LichtschrankeLesen		= 15	# Pin um Lichtschranke zu lesen
gpio_ReetSchalterLesen		= 14	# Pin um Reed Schlater zu lesen
gpio_windenMotorIn1			= 13	# Pin für die Winde. 4 Schritt Motor. In1
gpio_windenMotorIn2			= 12	# Pin für die Winde. 4 Schritt Motor. In2
gpio_windenMotorIn3			= 11	# Pin für die Winde. 4 Schritt Motor. In3
gpio_windenMotorIn4			= 10	# Pin für die Winde. 4 Schritt Motor. In4
#gpio_turmMotorIn1			= 9		# Pin für den Turm.  4 Schritt Motor. In1
#gpio_turmMotorIn2			= 8		# Pin für den Turm.  4 Schritt Motor. In2
#gpio_turmMotorIn3			= 7		# Pin für den Turm.  4 Schritt Motor. In3
#gpio_turmMotorIn4			= 6		# Pin für den Turm.  4 Schritt Motor. In4
gpio_weichenMotor			= 5		# Pin für den Turm.  4 Schritt Motor. In4
gpio_harkenAktivieren		= 3	# Pin um den Elektromagneten einzuschalten
gpio_turmMotor				= 4		# Pin für den Turm. Servo Motor
gpio_simulationsStellwReq	= 2		# Pin um eigene Stellwerksantwort zu senden. Nur zur Simmulation
gpio_stellwReq				= 1		# Pin schreibt anfrage Stellwerk ans stellwerk. Fallende Flanke wenn GPIIO 0 == 1. Ohne Stellwerk mit GPIO 1 verbinden
gpio_stellwAck				= 0		# Pin liesst Stellwerk antwort. Fallende Flanke Ok. Ohne Stellwerk mit GPIO 1 verbinden


# GLOBALEN
sensorUeberwachungLoopSleepTimeMs = 1
stepsHarken 					= 1500				# Hierüber lässt sich einstellen wie viel Faden von der Winde abgewickelt werden soll. Je größer desto mehr.
stepsHarkenOffset				= 150               # Hier lässt sich die einstellen wie viel mehr Faden gegeben werden muss um den Boden zu erreichen. Differnez Boden zu Wagon
delayHarken 					= float(0.002)		# Geschwindigkeit mit der der Faden abgerollt werden soll. 0.001 max geschwindigkeit
richtungHarkenHoch				= 1					# Winde wickelt Faden auf
richtungHarkenRunter			= -1				# Winde wickelt Faden ab
#stepsTurn180Grad				= 260				# Hierüber lässt sich einstellen wie weit der Turm gedreht werden soll. 220 ca 180 Grad.
#delayTurn						= float(0.005)		# Geschwindigkeit mit der der Turm rotieren soll. 0.001 max geschwindigkeit
#speedTurmmotor					= 0.02				# Geschwindigkeit mit der der Turm rotieren soll. Besser nicht ueber 0.02
richtungTurmDrehtRechts			= 1					# Turm dreht sich nach Rechts
richtungTurmDrehtLinks			= -1				# Turm dreht sich nach Links
gleisstromZugRein				= 1					# Wie rum sollen die Gleise unter Strom. 1 == Zug Rein, 0 == Zug Raus
gelisstromZugRaus				= 0					# Wie rum sollen die Gleise unter Strom. 1 == Zug Rein, 0 == Zug Raus
richtungWeicheAuf				= 1					# Weiche wird geoeffnet
richtungWeicheZu				= 0					# Weiche wird geschlossen
weichenMotorTraegerFrq			= 50				# Taeger Frequenz fuer Weichenmotor
endlageWeicheAuf				= 1500000			# PWM duty time fuer Weiche auf
endlageWeicheZu					= 1300000			# PWM duty time fuer Weiche zu
turmMotorGrad000				= 500000			# PWM duty fuer den Winkel des Turmmotors
turmMotorGrad090				= 1500000			# PWM duty fuer den Winkel des Turmmotors
turmMotorGrad180				= 2500000			# PWM duty fuer den Winkel des Turmmotors
speed_schrittweite_Turmmotor	= 10000				# Drehgeschwindigkeit Turmmotor in steps ns
verzoegerungTurmMotor			= 0.02				# Verlangsamt das drehen des Turmmotors
stellwSimulationTasteSteigendeFlanke = "s"
stellwSimulationTasteFallendeFlanke	 = "f"
minZugSpeed						= 45				# Min duty time fuer schwarzen zug zum bewegen. In Prozent. Wahrscheinlich zwischen 45% und 40% NOCH ZU TESTEN!!!
abbruchzeitZugErsterHaltepunkt 	= 50000				# In Ms. Nach dieser Zeit schaltet die H-Brücke ab. Damit Zug nicht zuweit fährt. Kann auch genutzt werden,
                                                    # wenn Reed kontakt nicht ordentlich greift. Dann kann versucht werden über diesen Parameter den Zug unter
                                                    # den Kran zu stellen. Zeit in Millisekunden. WERT MUSS NOCH DURCH TESTEN RAUSGEFUNDEN WERDEN
abbruchzeitZugZweiterHaltepunkt = 1000
abbruchzeitZugVerlaesstBereich  = 30000
                                           



