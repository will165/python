import random
import os
import itertools
import math

def getDados():
	spam = []
	linhas = open('spambase.data','r')
	for line in linhas:
		x = line.replace("\n","")
		x = x.split(",")
		spam.append(x)
	return spam


def selectTeste(n=20):
	#Gera uma matriz para testes
	z = int(len(spamList)*(n/100))
	spamTest = spamList[:z]
	del spamList[:z]
	return spamTest


def calcDistancia(spam1,spam2):
	c = [math.pow(float(x)-float(y),2) for x,y in zip(spam1[:57], spam2[:57])]
	return math.sqrt(sum(c))

#def calcDistancia(spam1,spam2):
#	somatorio = 0.0
#	for x in range(57):#trocar para 57
#		somatorio += math.pow((float(spam1[x])-float(spam2[x])),2)
#	return math.sqrt(somatorio)

def classificar(classList):
	nSpam = classList.count(str(1))
	nNotSpam = classList.count(str(0))
	if nNotSpam > nSpam:
		return 0
	else:
		return 1

#Lista de treino, lista de testes, qtd de vizinhos
def knn(spamList,testeList,qtdVizinhos=3):
	i = 0
	d = 0
	a = 0
	b = 0
	c = 0
	nAcertos = 0;
	for teste in testeList:
		menores_distancias = [math.inf]*qtdVizinhos
		classe = [None]*qtdVizinhos
		for spam in spamList:
			maiorNumero = menores_distancias.index(max(menores_distancias))
			n = calcDistancia(teste,spam)
			if menores_distancias[maiorNumero] > n:
				menores_distancias[maiorNumero] = n
				classe[maiorNumero] = spam[-1]

		e = classificar(classe)
		if int(e) == int(teste[-1]):
			nAcertos = nAcertos + 1
			if int(e) == 1:
				#positivo positivo (d)
				d += 1
			else:
				#negativo negativo (a)
				a += 1
		else:
			if int(e) == 1:
				#positivo negativo (b)
				b += 1
			else:
				#negativo positivo (c)
				c += 1
		i = i+1
		printProgressBar(i, tamanho, prefix = 'Progresso:', suffix = 'Completa', length = 50)
	percent = (nAcertos/int(len(testeList)))*100
	print(str(round(percent,2)) + "% de acertos" )
	printMatrizConfusao(a,b,c,d)
	return str(round(percent,2)) + "% de acertos"

def printMatrizConfusao(a,b,c,d):
	matriz = [["","","","Predicted"],["","","Negative","Positive"],["","Negative",a,b],["","Positive",c,d]]
	print("%s\t%s%s\t%s"% (matriz[0][0],matriz[0][1],matriz[0][2],matriz[0][3]))
	print("%s\t%s\t%s|%s"% (matriz[1][0],matriz[1][1],matriz[1][2],matriz[1][3]))
	print("%s\t%s\t%s\t%s"% (matriz[2][0],matriz[2][1],matriz[2][2],matriz[2][3]))
	print("%s\t%s\t%s\t%s"% (matriz[3][0],matriz[3][1],matriz[3][2],matriz[3][3]))



def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()

spamList = getDados()
#Embaralha as linhas da matriz de maneira aleatória
random.shuffle(spamList)
print("Qual a % para testes?")
percentTestes = int(input()) #n classes + 1

testeList = selectTeste(percentTestes)# TODO: TROCAR O 1
tamanho = int(len(testeList))
print("Qual o numero de vizinhos?")
qtdVizinhos = int(input()) #n classes + 1
printProgressBar(0, int(len(testeList)), prefix = 'Progresso:', suffix = 'Completa', length = 50)
knn(spamList,testeList,qtdVizinhos)

#printMatrizConfusao('a','b','c','d')
kList = [1,3,5,7]
listaResp = []
for x in kList:
	listaResp.append(knn(spamList,testeList,x))
print(listaResp)
