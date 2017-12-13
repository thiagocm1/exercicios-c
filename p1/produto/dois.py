numero_1 = raw_input()
numero_2 = raw_input()
par = []
impar = []
for x in numero_1:
	if x % 0 == 0:
		par.append(x)
		print x
	else:
		impar.append(x)
		print x
