#coding:  utf-8
sal = float(raw_input())
aumento = float(raw_input())/100
inss = float(raw_input())/100
print "Dados do novo salário"
sal1 = sal+ aumento*sal
inss1 = inss*sal1
sal_liq = sal1 - inss1
print "Dados do novo salário"
print " ==="
print "Salário: R$ %.2f" % sal1
print "Contribuição previdenciária: R$ %.2f (%.2f)" % (inss1, inss)
print "Salário líquido: R$ %.2f" % sal_liq
