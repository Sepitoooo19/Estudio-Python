


diccionario = {

    "nombre" : "Benja",
    "apellido" : "Sepulveda",
    "edad" : 21

}

print("")
print("Claves del diccionario")
claves = diccionario.keys() #Devuelve las claves del diccionario, tambien sirve para iterar
print(claves)
print("")

print("Valores para la clave 'nombre' ")
valores = diccionario.get("nombre") #Dvuelve los valores de las claves
print(valores)
print("")

print("Valores para la clave 'apellido")
valores = diccionario.get("apellido")
print(valores)
print("")

print("Valores para la clave 'edad'")
valores = diccionario.get("edad")
print(valores)
print("")
#diccionarioEliminado = diccionario.clear() #Descomentando esto se elimina el diccionario creado anteriormente
#print(diccionarioEliminado)


print("Eliminando clave 'nombre' con pop()")
diccionario.pop("nombre")
print(diccionario)
print("")


print("Iterables de un diccionario con items()")

diccionarioIterable = diccionario.items()
print(diccionarioIterable)





