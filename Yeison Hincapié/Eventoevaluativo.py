
import random

FILAS = 5
COLUMNAS = 5

# Elegir dificultad
dificultad = input("Elige la dificultad (F=Fácil, M=Medio, D=Difícil): ").upper()
while dificultad not in ["F", "M", "D"]:
    print("Error, no se encontró la dificultad elegida.")
    dificultad = input("Elige la dificultad (F, M, D): ").upper()

if dificultad == "F":
    intentos_max = 10
elif dificultad == "M":
    intentos_max = 7
else:  # dificultad == "D"
    intentos_max = 4

matriz = [["-" for _ in range(COLUMNAS)] for _ in range(FILAS)]

tesoro_x = random.randint(0, FILAS - 1)
tesoro_y = random.randint(0, COLUMNAS - 1)
matriz[tesoro_x][tesoro_y] = "T"

for _ in range(3):
    while True: 
        trampa_x = random.randint(0, FILAS - 1)
        trampa_y = random.randint(0, COLUMNAS - 1)
        if matriz[trampa_x][trampa_y] == "-":
            matriz[trampa_x][trampa_y] = "X"
            break
intentos = 0
encontrado = False

# Solicitar coordenadas al usuario
while True:
    try: 
        x = int(input("ingrese la coordenada X (0-4): "))
        y = int(input("ingrese la coordenada Y (0-4): "))
        if 0 <= x < FILAS and 0 <= y < COLUMNAS:
            if matriz[x][y] == "T":
                print("Has encontrado el tesoro!")
                matriz[x][y] = "T"
                break
            elif matriz[x][y] == "X":
                print("Has pisado una trampa! Juego terminado.")
                matriz[x][y] = "X"
                break
            else: 
                print("No has encontrado nada. Sigue buscando.")
                matriz[x][y] = "O"
        else:
            print("Coordenadas fuera de rango. Intenta de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor ingresa números entre 0 y 4.")

  
    intentos += 1
    if not encontrado and intentos >= intentos_max:
     print("\n¡Se acabaron tus intentos!")
        

# Mostrar el tablero final
print("Tablero final:")
for fila in matriz:
    print(" ".join(fila))
    break
# Fin del jue
