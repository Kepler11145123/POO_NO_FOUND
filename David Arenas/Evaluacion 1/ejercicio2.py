import random

# Crear matriz 5x5 llena de guiones
tablero = [["-" for _ in range(5)] for _ in range(5)]

# Colocar el tesoro (T)
tesoro_fila = random.randint(0, 4)
tesoro_col = random.randint(0, 4)
tablero[tesoro_fila][tesoro_col] = "T"

# Colocar 3 trampas (X)
trampas_colocadas = 0
while trampas_colocadas < 3:
    f = random.randint(0, 4)
    c = random.randint(0, 4)
    if tablero[f][c] == "-":
        tablero[f][c] = "X"
        trampas_colocadas += 1

# Juego
while True:
    print("\nIngresa una coordenada para buscar (0-4 en fila y columna)")
    fila = int(input("Fila: "))
    col = int(input("Columna: "))

    if tablero[fila][col] == "-":
        print("No encontraste nada, intenta de nuevo.")
    elif tablero[fila][col] == "X":
        print("💀 ¡Pisaste una trampa! Perdiste el juego.")
        break
    elif tablero[fila][col] == "T":
        print("🎉 ¡Encontraste el tesoro! Ganaste el juego.")
        break

# Mostrar tablero completo al final
print("\nTablero final:")
for fila in tablero:
    print(" ".join(fila))
