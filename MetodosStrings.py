


print("Cadenas")

cadena1 = "Hola soy Benja"
cadena2 = "Mi apellido es Sepulveda"
print(cadena1)
print(cadena2)
print("")

print("Metodos de String: ")
print("Metodo upper(): ") #Convierte a Mayuscula el string
resultado = cadena1.upper()
resultado2 = cadena2.upper()
print(resultado)
print(resultado2)
print("")

print("Metodo lower(): ")   #Convierte a minuscula el string
resultado = cadena1.lower()
resultado2 = cadena2.lower()
print(resultado)
print(resultado2)
print("")

print("Metodo capitalize(): ")  #Solo la primera letra en mayuscula
resultado = cadena1.capitalize()
resultado2 = cadena2.capitalize()
print(resultado)
print(resultado2)
print("")

print("Metodo find(): ")
resultado = cadena1.find("Hola") #Primera ocurrencia del valor a buscar, si no devuelve -1
resultado2 = cadena2.find("x")
print(resultado)
print(resultado2)
print("")

print("Metodo find(): ")
resultado = cadena1.index("Hola") #Primera ocurrencia del valor a buscar, si no devuelve error
#resultado2 = cadena2.index("x")
print(resultado)
#print(resultado2)
print("")

print("Metodo isnumeric(): ") #verifica si es un numero
resultado = cadena1.isnumeric()
print(resultado)
print("")

print("Metodo isalpha(): ") #Verifica si es alfa numerico (de la a a la z, sin contar los espacios)
resultado = cadena1.isalpha()
print(resultado)
print("")

print("Metodo count(): ") #Cuenta las ocurrencias del valor dado
resultado = cadena1.count("a")
print(resultado)
print("")

print("Metodo len(): ") #Largo del string
resultado = len(cadena1)
print(resultado)
print("")

print("Metodo startswith(): ")
resultado = cadena1.startswith("H") #verifica si la cadena empieza con una cadena dada
print(resultado)
print("")

print("Metodo endswith(): ")
resultado = cadena1.endswith("a") # Verifica si la cadena termina con una cadena dada
print(resultado)
print("")

print("Metodo replace(): ")
resultado = cadena1.replace("H", "e") #reemplaza un valor de la cadena por otro valor dado
print(resultado)
print("")

print("Metodo split(): ")
resultado = cadena1.split("a")  #separa los elementos de la cadena con el valor dado y devuelve una lista
print(resultado)



