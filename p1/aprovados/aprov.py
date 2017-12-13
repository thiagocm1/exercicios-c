# coding: utf-8
print "Análise de Aprovação"
print "==="
n1 = float(raw_input("Número de Aprovados ? "))
n2 = float(raw_input("Número de Reprovados ? "))
total = n1 + n2
print "---"
n1 = (n1)*100/total
n2 = (n2)*100/total
print "Total de Alunos na turma: %i" % total
print "Aprovados: %i = %.1f" % (n1,n1)
print "Reprovados %i = %.1f" % (n2,n2)





