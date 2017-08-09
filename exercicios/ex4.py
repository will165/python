def fun(numero,expoente=2):
	temp = 1
	for i in range(expoente):
		temp *= numero
	return temp

print(fun(2))
print(fun(10))
print(fun(2,9))
