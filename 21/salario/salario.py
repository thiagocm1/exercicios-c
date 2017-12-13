#coding:utf-8
#UFCG - Programação I / Portas Eletrônicas
#Thiago Montenegro - 2015.2
while True:
	entrada = raw_input().split()
	registro = entrada[0]
	tipo = entrada[-1]
	if registro == 'S':
		
		break
	elif registro == 'R':
		registros.append(tipo[0])
	elif registro == 'P':
		cont = 0
		for i in registros:
			if i == tipo[0]:
				cont += 1
			
		print cont
		
