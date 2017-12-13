#coding: utf-8
nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())
peso1 = float(raw_input())/100
peso2 = float(raw_input())/100
peso3 = 1.0 - (peso2+peso1)
media_final = peso1*nota1 + peso2*nota2 + peso3*nota3

print "Média Final: %.1f" % media_final


