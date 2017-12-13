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
	if x[0] == "a":
		vogais.append(consoante)
	elif x[0] == "e":
		vogais.append(consoante)
	elif x[0] == "i":
		vogais.append(consoante)
	elif x[0] == "o":
		vogais.append(consoante)
	elif x[0] == "u":
		vogais.append(consoante)
	else:
		consoantes.append(consoante)
print consoantes
print vogais
conta = len(consoantes)			
media = len(consoantes)/float(len(vogais))
media = media * 100
print media
print "total de palavras: %d" % (quantas_palavras)
print "iniciadas por consoante: %d (%.2f%%)" % (conta, media)
