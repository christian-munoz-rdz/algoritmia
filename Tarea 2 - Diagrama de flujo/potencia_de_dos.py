#Comprobamos si un numero es potencia de dos

def es_potencia_de_dos(numero): 
    while numero % 2 == 0:
        numero = numero / 2
    if numero == 1:
        return True
    else:
        return False

def main():
    numero = int(input("Introduce un numero: "))
    if es_potencia_de_dos(numero):
        print("Es potencia de dos")
    else:
        print("No es potencia de dos")

if __name__ == "__main__":
    main()