
import random

dificultad = int(input("ingrese el numero de intentos por partida que desea del 1 al 5: "))

# Crear una matriz de 5x5 llena de guiones
matriz = [['-' for _ in range(5)] for _ in range(5)]

# Lista de elementos que quieres colocar (ahora con 3 'X's)
elementos = ['T', 'X', 'X', 'X']

# Obtener todas las posibles coordenadas (fila, columna)
coordenadas_disponibles = [(f, c) for f in range(5) for c in range(5)]

# Seleccionar 5 coordenadas aleatorias (una para cada elemento)
coordenadas_aleatorias = random.sample(coordenadas_disponibles, 5)

# Colocar los elementos en las coordenadas seleccionadas

for i in range(4):
    fila, columna = coordenadas_aleatorias[i]
    matriz[fila][columna] = elementos[i]
for fila in matriz:
    print(' '.join(fila))
for i in range(1,dificultad+1):
    primera_cordenada = int(input("ingrese la fila: "))
    segunda_cordenada = int(input("ingrese la columna"))
    if matriz[primera_cordenada][segunda_cordenada] == '-':
        print("prueba otra coordenada")
    elif matriz[primera_cordenada][segunda_cordenada] == 'T':
        print("FELICIDADES HAS GANADO")
        break
    elif matriz[primera_cordenada][segunda_cordenada] == 'X':
        print("has perdido encontraste una X")
        break




# Imprimir la matriz

for fila in matriz:
    print(' '.join(fila))