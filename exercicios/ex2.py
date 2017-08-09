lista = []
for i in range(3):
	lista.append(input())

print(max(lista))
print(min(lista))

theSum = 0
for i in lista:
    theSum = theSum + int(i)
print(theSum)
