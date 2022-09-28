#Busqueda lineal en un vector
import random

def busqueda_lineal(vector, objetivo):
    i = 0 # 1
    encontrado = False # 1

    while (i < len(vector)-1) and (vector[i] != valor): #4n
        i += 1 # n-1
    
    if vector[i] == valor: # 1
        encontrado = True #1
    
    return encontrado #1

#T(n) = 1 + 1 + 4n + n-1 + 1 + 1 + 1 = 5n + 4

if __name__ == "__main__":
    #Generar un vector de 100 elementos
    vector = [random.randint(0, 100) for i in range(100)]
    #ingresar el valor a buscar
    valor = int(input("Ingrese el valor a buscar: "))

    #Busqueda lineal
    encontrado = busqueda_lineal(vector, valor)

    #Imprimir el resultado
    print(f"El valor {valor} {'esta' if encontrado else 'no esta'} en el vector")

    




