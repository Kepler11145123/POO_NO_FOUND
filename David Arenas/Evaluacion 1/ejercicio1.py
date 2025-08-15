# Solicitar dimensiones
entrada = input("Ingrese fila y columna en enteros en el siguiente formato 3,4: ")
filas, columnas = map(int, entrada.split(','))

# Crear matriz con números sucesivos
matriz = []
valor = 1
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(valor)
        valor += 1
    matriz.append(fila)

# Mostrar matriz original
print("\nMatriz original:")
for fila in matriz:
    print(fila)

# Crear matriz modificada (filas impares invertidas)
matriz_modificada = []
for i in range(filas):
    if i % 2 == 0:  # fila par → normal
        matriz_modificada.append(matriz[i][:])
    else:  # fila impar → invertida
        matriz_modificada.append(list(reversed(matriz[i])))

# Mostrar matriz con filas impares invertidas
print("\nMatriz con filas impares invertidas:")
for fila in matriz_modificada:
    print(fila)