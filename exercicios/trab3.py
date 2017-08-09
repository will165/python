import matplotlib.pyplot as plt
import time

def main():
    f = open('testCase1.txt', 'r')
    aux = [int(x) for x in f.readline().split()]
    fig, ax = plt.subplots()
    ax.set_xlim((0, aux[0]))
    ax.set_ylim((0, aux[1]))
    nCircles = int(f.readline())
    cList = [] #lista de cículos, dada pelos seus raios.
    for i in range(nCircles):
        radius = int(f.readline())
        cList.append(radius)
    cList.sort() #O(nlgn)
    #start = time.time()
    insertCircles(cList, fig, ax, aux[0], aux[1])#Através de resultados obtidos por testes, aparente se comportar com complexidade O(n).
    #end = time.time()
    #print(end-start)
    
def insertCircles(cList, fig, ax, xlim, ylim):
    '''
    A inserção começa do canto esquerdo inferior do retângulo. Vai adicionando
    círculos daquele com menor raio pro maior. Se o círculo a ser adicionado não
    couber, o algoritmo traça uma linha imaginária a uma altura igual ao diâmetro
    do maior círculo inserido neste espaço.
    '''
    currentx = 0
    currentyLine = 0
    for c in cList:
        diam = 2*c
        if currentx+diam <= xlim and currentyLine+diam <= ylim:
            circle = plt.Circle((currentx+c, currentyLine+c), c, color='r')
            currentx += diam
        elif currentx+diam > xlim:
            currentx = 0
            currentyLine += diam
            if currentyLine+diam > ylim:
                continue
            circle = plt.Circle((currentx+c, currentyLine+c), c, color='r')
            currentx += diam
        ax.add_artist(circle)
        
    fig.savefig('circles.png')
    #plt.show() 

if __name__ == "__main__":
    main()
