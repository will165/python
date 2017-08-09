#Exercicio 1#
x = input()
for i in x:
	print(str(i).lower())
#Exercicio 2#
lista = []
for i in range(3):
	lista.append(input())

print(max(lista))
print(min(lista))

theSum = 0
for i in lista:
    theSum = theSum + int(i)
print(theSum)


#Exercicio 3#
for i in range(10,100):
	if i%5 == 0:
		print(i)

#Exercicio 4#
def fun(numero,expoente=2):
	temp = 1
	for i in range(expoente):
		temp *= numero
	return temp

print(fun(2))
print(fun(10))
print(fun(2,9))


#Exercicio 5#
def fun(*numeros):
	lista = []
	for x in numeros:
		lista.append(x*x)
	return lista

print(fun(10,5,8,4))



#FLOWERS PROBLEMA DA AULA 2 #
class Flower(object):
	def __init__(self, ide,sepal_length_cm,sepal_width_cm,petal_length_cm,petal_width_cm,species):

		self.ide = ide
		self.sepal_length_cm = sepal_length_cm
		self.sepal_width_cm = sepal_width_cm
		self.petal_length_cm = petal_length_cm
		self.petal_width_cm = petal_width_cm
		self.species = species

	def __str__(self):
		return "Especie: " + str(self.species)+"\n"+"Sepal Lenght: " + str(self.sepal_length_cm)+"\n"+"Sepal Width: " + str(self.sepal_width_cm)+"\n"+"Petal Lenght: " + str(self.petal_length_cm)+"\n"+"Petal Width: " + str(self.petal_width_cm)+"\n"


if __name__ == '__main__':
	flowers = []
	linhas = open('iris.data');
	array = []
	i = 0;
	for line in linhas:
		x = line.replace("\n","")
		x = x.split(",")
		if(len(x) > 4):
			flowers.append(Flower(i,x[0],x[1],x[2],x[3],x[4]))
		i = i+1

	for a in flowers:
		print(a)
