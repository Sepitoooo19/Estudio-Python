
print("Diccionario creado")
diccionario = {

    "nombre" : "Benja",
    "apellido" : "Sepulveda",
    "edad": 21


}
print(diccionario)
print("")

print("Recorriendo las claves del diccionario")
for key in diccionario:
    print(key)

print("")
print("Recorriendo el diccionario con items()")
for key in diccionario.items():
    print(key)

print("")

print("Recorriendo el mismo diccionario, pero con asignaciones")
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'la clave {key} es y su valor es: {value}')

