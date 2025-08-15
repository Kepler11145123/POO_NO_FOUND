def contar_vocales():
    
    
    cadena = input("Por favor, ingresa una cadena de texto: ")
    
    cadena = cadena.lower()

    
    conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    
    for caracter in cadena:
        if caracter in conteo_vocales:
            conteo_vocales[caracter] += 1

    
    

    

    while True:
        # Preguntar al usuario por la vocal que desea consultar
        vocal_a_consultar = input("\n¿Qué vocal te gustaría consultar? (a, e, i, o, u) o escribe 'salir' para terminar: ").lower()

        # Salir del bucle si el usuario lo desea
        if vocal_a_consultar == 'salir':
            print("¡Hasta luego!")
            break

        
        if vocal_a_consultar in conteo_vocales:
            cantidad = conteo_vocales[vocal_a_consultar]
            print(f"La vocal '{vocal_a_consultar}' se repitió {cantidad} veces en la cadena.")
        else:
            print("Entrada no válida. Por favor, ingresa una de las vocales (a, e, i, o, u).")

# Ejecutar la función
contar_vocales()