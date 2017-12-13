nota_1 = float(raw_input())
nota_2 = float(raw_input())
nota_3 = float(raw_input())
faltas = int(raw_input())
media = (nota_1 + nota_2 + nota_3)/3
if (faltas > 7):
	print "reprovado por faltas"
else:
	if media >= 7:
		print "aprovado por media"
	elif media <= 7 and media <= 4:
		 print "reprovado por nota"
	elif 4.0 < media < 7.0:
		print "prova final"
	 
	 
	 
	
	

		
		
		

