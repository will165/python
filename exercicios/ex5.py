def fun(*numeros):
	lista = []
	for x in numeros:
		lista.append(x*x)
	return lista

print(fun(10,5,8,4))
