
Vocales = "aeiou"
contador_vocales = {}
cadena = input("Ingrese una cadena de texto: ")
cadena = cadena.lower() 
for letra in cadena:
    if letra in Vocales:
        if letra in contador_vocales:
            contador_vocales[letra] += 1
        else:
            contador_vocales[letra] = 1 
