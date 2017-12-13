placa = raw_input()
placas = []
for mes in placa:
	if placa[6] == 1 or placa[6] == 2:
		print "%s:  janeiro" %(mes)
	elif placa[6] == 3 or placa[6] == 3:
		print "%s:  fevereiro" %(placa)
	elif placa[6] == 5:
		print "%s:  marco" %(placa)
	elif placa[6] == 6:
		print "%s: abril" %(placa)
	elif placa[6] == 7:
		print "%s:  maio" %(placa)
	elif placa[6] == 8:
		print "%s:  junho" %(placa)
	elif placa[6] == 9:
		print "%s: julho" %(placa)
	elif placa[6] == 0:
		print "%s:  agosto" %(placa)
	print mes	
