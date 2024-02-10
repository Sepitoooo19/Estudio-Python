

frase = input("Dime una frase y te calculo cuanto tardarias si tuvieses que decirla: ")

palabrasSeparadas= frase.split(" ")

cantidadPalabras = len(palabrasSeparadas)


if cantidadPalabras > 120:
    print("Tampoco un texto tan largo")


print(f"dijiste: {cantidadPalabras} palabras, y tardarias {cantidadPalabras/2} segundos en decirlo")
print(f"El sepu tardaría {cantidadPalabras/2*1.3} segundos en decirlo  ")

