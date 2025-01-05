from machine import Pin

gpio_harkenAktivieren		= 16	# Pin um den Elektromagneten einzuschalten
gpio_LichtschrankeLesen		= 15	# Pin um Lichtschranke zu lesen
gpio_ReetSchalterLesen		= 14	# Pin um Reed Schlater zu lesen
gpio_windenMotorIn1			= 13	# Pin für die Winde. 4 Schritt Motor. In1
gpio_windenMotorIn2			= 12	# Pin für die Winde. 4 Schritt Motor. In2
gpio_windenMotorIn3			= 11	# Pin für die Winde. 4 Schritt Motor. In3
gpio_windenMotorIn4			= 10	# Pin für die Winde. 4 Schritt Motor. In4
gpio_turmMotorIn1			= 9		# Pin für den Turm.  4 Schritt Motor. In1
gpio_turmMotorIn2			= 8		# Pin für den Turm.  4 Schritt Motor. In2
gpio_turmMotorIn3			= 7		# Pin für den Turm.  4 Schritt Motor. In3
gpio_turmMotorIn4			= 6		# Pin für den Turm.  4 Schritt Motor. In4
gpio_weichenMotor			= 5		# Pin für den Turm.  4 Schritt Motor. In4
gpio_stellwReq				= 1		# Pin schreibt anfrage Stellwerk ans stellwerk. Fallende Flanke wenn GPIIO 0 == 1. Ohne Stellwerk mit GPIO 1 verbinden
gpio_stellwAck				= 0		# Pin liesst Stellwerk antwort. Fallende Flanke Ok. Ohne Stellwerk mit GPIO 1 verbinden


# GLOBALEN
stepsHarken 			= 1500				# Hierüber lässt sich einstellen wie viel Faden von der Winde abgewickelt werden soll. Je größer desto mehr.
delayHarken 			= float(0.002)		# Geschwindigkeit mit der der Faden abgerollt werden soll. 0.001 max geschwindigkeit
richtungHarkenHoch		= 1					# Winde wickelt Faden auf
richtungHarkenRunter	= -1				# Winde wickelt Faden ab
stepsTurn180Grad		= 260				# Hierüber lässt sich einstellen wie weit der Turm gedreht werden soll. 220 ca 180 Grad.
delayTurn				= float(0.005)		# Geschwindigkeit mit der der Turm rotieren soll. 0.001 max geschwindigkeit
richtungTurmDrehtRechts	= 1					# Turm dreht sich nach Rechts
richtungTurmDrehtLinks	= -1				# Turm dreht sich nach Links
gleisstromZugRein		= 1					# Wie rum sollen die Gleise unter Strom. 1 == Zug Rein, 0 == Zug Raus
gelisstromZugRaus		= 0					# Wie rum sollen die Gleise unter Strom. 1 == Zug Rein, 0 == Zug Raus
richtungWeicheAuf		= 1					# Weiche wird geoeffnet
richtungWeicheZu		= 0					# Weiche wird geschlossen
weichenMotorTraegerFrq	= 50				# Taeger Frequenz fuer Weichenmotor
endlageWeicheAuf		= 1500000			# PWM duty time fuer Weiche auf
endlageWeicheZu			= 1300000			# PWM duty time fuer Weiche zu




