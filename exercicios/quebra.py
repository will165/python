solution = [1,2,3,4,5,"",6,7,8]
print(lista)
print("\t|3|4|6|")
print("\t|2| |5|")
print("\t|1|8|7|")

class Pluzze(object):
	def __init__(self, *numeros):
		self.numeros = numeros

	def __str__(self):
		return()