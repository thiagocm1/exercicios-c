entrada = float(raw_input())
if entrada >= 360:
	calculo = entrada - 360
	if  0 < calculo < 90:
		print "Quadrante 1" 
	elif 90 < calculo < 180:
		print "Quadrante 2"
	elif 180 < calculo < 270:
		print "Quadrante 3"
	elif 270 < calculo < 360:
		print "Quadrante 4"
	else:
		"Sobre eixos"
		
else:
	if 0 < entrada < 90:
		print "Quadrante 1"
	elif 90 < entrada < 180:
		print "Quadrante 2"
	elif 180 < entrada < 270:
		print "Quadrante 3"
	elif 270 < entrada < 360:
		print "Quadrante 4"
	else:
		print "Sobre eixos"
