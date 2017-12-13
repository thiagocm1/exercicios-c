#coding:utf-8
#UFCG - Programação I / Nome 3 vezes
#Thiago Montenegro - 20.15
print "== Estágio 1 =="
peso = float(raw_input("Peso? "))
nota = float(raw_input("Nota? "))
print "== Estágio 2 =="
peso1 = float(raw_input("Peso? "))
nota1 = float(raw_input("Nota? "))
print "== Estágio 3 =="
peso2 = float(raw_input("Peso? "))
nota2 = float(raw_input("Nota? "))
print "== Resultados =="
media = (nota*peso) + (nota1*peso1) + (nota2*peso2)
print "Média parcial: %.1f" % (media)
print "Nota na final, pra média 5.0 = %.1f" % ((((media*0.6)-5)/0.4)*-1)
print "Nota na final, pra média 7.0 = %.1f" % ((((media*0.6)-5)/0.4)*(-1)+5) 
