
class Mamifero(object):
	"""Esse objeto represe4nta mamiferos"""
	def __init__(self, arg, peso=50):
		super(Mamifero, self).__init__()
		self.arg = arg
		self.peso = peso


	def metodo(self):
		"""Faz nada"""
		print(self.arg)

	def __add__(self, other):
		return self.arg + other.arg

	def __mul__(self, other):
		return (self.arg + other.arg)*5

	def __str__(self):
		return str(self.arg)

	def __repr__(self):
		return str('"' + self.arg + '"' + str(self.peso))

if __name__ == '__main__':
	a = Mamifero('b')
	b = Mamifero('a')

	print([a,b])

