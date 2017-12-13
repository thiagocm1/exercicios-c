#coding: utf-8
#UFCG - Programação I / Thiago Cunha
#Classifica Letra como Vogal ou Consoante
palavra = raw_input()
for x in palavra:
	if x == "a" or x == "A" :
		vogal = x
		print "<%s> sim" %(vogal)
	elif x == "e" or x == "E" :
		vogal = x
		print "<%s> sim" %(vogal)
	elif x == "i" or x == "I":
		vogal = x
		print "<%s> sim" %(vogal)
	elif x == "o" or x == "O":
		vogal = x
		print "<%s> sim" %(vogal)
	elif x == "u" or x == "U":
		vogal = x	
		print "<%s> sim" %(vogal)
	else:
		consoante = x
		print "<%s> nao" %(consoante)
		




