#coding:utf-8
#UFCG - Programacao I
#Thiago Montenegro - 2015.2
nota = float(raw_input())
mts = int(raw_input())
if mts == 1:
	print "%.1f. Ainda não aprovado."  % (nota)
if mts > 1:
	nota_1 = float(raw_input())
	media = nota*(0.6) + nota_1 * (0.4)
	if media >= 6.0:
		print "%.1f. Aprovado." % (media)
	elif media < 6.0:
		print "%.1f. Ainda não aprovado." % (media)
