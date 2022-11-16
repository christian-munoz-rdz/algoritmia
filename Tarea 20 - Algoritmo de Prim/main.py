def prim(grafo):
    visitados = []
    arbol = []
    visitados.append(list(grafo.keys())[0])
    while len(visitados) < len(grafo):
        menor = 1000000 
        for i in visitados: 
            for j in grafo[i]: 
                if j not in visitados and grafo[i][j] < menor: 
                    menor = grafo[i][j]
                    nodo1 = i 
                    nodo2 = j 
        visitados.append(nodo2) 
        arbol.append((nodo1, nodo2))
    return arbol 

def main():
    grafo = {
        'C':{'A':2, 'B':8, 'D':5, 'E':3},
        'A':{'B':4, 'C':2},
        'B':{'A':4, 'C':8, 'D':7, 'E':9},
        'D':{'B':7, 'C':5, 'E':3, 'F':6},
        'E':{'B':9, 'C':3, 'D':3, 'F':1},
        'F':{'D':6, 'E':1}
    }
    print(prim(grafo))

if __name__ == "__main__":
    main()

'''
Resultado:
[('C', 'A'), ('C', 'E'), ('E', 'F'), ('E', 'D'), ('A', 'B')]
'''