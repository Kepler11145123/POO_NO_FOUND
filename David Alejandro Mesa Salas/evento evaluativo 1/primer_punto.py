
filas=int(input("ingrese el numero de filas que desea que tenga la matriz: "))
columnas=int(input("ingrese el numero de columnas que desea que tenga la matriz: "))

matriz = []
numero_actual = 1

# Llenar la matriz con números sucesivos
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(numero_actual)
        numero_actual += 1
    matriz.append(fila)

# Imprimir la matriz
print("\nLa matriz creada es:")
for fila in matriz:
    print(fila)

print("\nLa matriz con lectura alternada:")
for i, fila in enumerate(matriz):
    if i % 2 == 0:  
        print(fila)
    else:  
        print(fila[::-1])  
