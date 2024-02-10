

#Creando diccionarios con dict
print("Diccionario creado con dict()")
diccionario = dict(nombre = "Benja", apellido = "Sepulveda", edad = 21)
print(diccionario)

#Las listas no pueden ser claves y usamos frozenset para meter conjuntos
print("")

print("Creando diccionarios con fromkeys(), esto hace que los valores de las claves del diccionario sean 'none' ")
diccionario = dict.fromkeys(["nombre", "apellido"])
print(diccionario)
