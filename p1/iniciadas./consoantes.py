#coding: utf-8
#UFCG 
#Thiago Cunha Montenegro / Programação I
# Iniciadas por Consoantes
quantas_palavras = int(raw_input())
consoantes = []
vogais = []
for x in range(quantas_palavras):
	x = raw_input()
	consoante = x[0]
	if x[0] == "a" or x[0] == "A":
		vogais.append(consoante)
	elif x[0] == "e" or x[0] == "E":
		vogais.append(consoante)
	elif x[0] == "i" or x[0] == "I":
		vogais.append(consoante)
	elif x[0] == "o" or x[0] == "O":
		vogais.append(consoante)
	elif x[0] == "u" or x[0] == "U":
		vogais.append(consoante)
	else:
		consoantes.append(consoante)
conta = len(consoantes)			
media = len(consoantes) * 100.0 /quantas_palavras 
print "total de palavras: %d" % (quantas_palavras)
print "iniciadas por consoantes: %d (%.2f%%)" % (conta, media)
