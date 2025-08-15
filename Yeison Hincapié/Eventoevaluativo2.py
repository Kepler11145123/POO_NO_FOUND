#Dadas las dimensiones de una matriz de nxm, mostrar los indices de la matriz en forma horizontal

n=int(input("Ingrese el número de filas (n): "))
m=int(input("Ingrese el número de columnas (m): "))

def indices(n, m):
    for i in range(n):
        fila = [f"({i},{j})" for j in range(m)]
        print(' '.join(fila))

print("Este es el orden de sus índices:")
print(indices(n, m))

