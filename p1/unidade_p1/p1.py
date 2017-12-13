nota = float(raw_input())
if nota <= 0:
	nota = float(raw_input()
else:
	mt = int(raw_input())
	if mt == 1:
		media = nota * 0.60
		print "%.1f. Ainda não aprovado." % (media)
	else:
		nota_2 = float(raw_input()
		media = (nota * 0.60 + nota_2 * 0.40) / 2 
		if media >= 7.0:
			print  "%.1f. Aprovado." % (media)
		else:
			print "%.1f. Ainda não aprovado." % (media)

		
	
			
	
