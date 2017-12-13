#coding: utf-8
#Classificação dos Elementos Utilizando a Média dos Extremos
#UFCG - Programação I / Thiago Cunha
n = int(raw_input())
lista_num = []
for x in range(n):
	sequencia = float(raw_input())
	lista_num.append(sequencia)
menor = lista_num[0]
maior = lista_num[0]
for numero in lista_num:
	if numero <= menor:
		menor = numero
	if numero >= maior:
		maior = numero
media = (maior + menor) / 2
menor_media = 0
maior_media = 0
for numero_2 in lista_num:
	if numero_2 > media:
		maior_media += 1
	elif numero_2 < media:
		menor_media += 1
print "Menor número: %d" % (menor)
print "Maior número: %d" % (maior)
print "Média dos extremos: %.2f" % (media)
print "%d número(s) abaixo da média" % (menor_media)
print "%d número(s) acima da média" % (maior_media)
		
	
