
#Una lista es un conjunto de datos
print("Lista")
lista = ["Benja", "Sepulveda", 21]
print(lista)

# Las listas parten de la posicion 0, la posicion 0 indica el primer elemento de la lista
print(lista[0]) #elemento uno = posicion 0 de la lista
print(lista[1]) #elemento dos = posicion 1 de la lista
print(lista[2]) #elemento tres = posicion 2 de la lista
print("Modificando elementos de lista ( lista[2] = 22 )")
lista[2] = 22
print(lista)

# Tupla, son conjuntos de datos, al igual que las listas pero no se pueden modificar
print("")
print("Tupla")
tupla = ("Benja", "Sepulveda", 21)
print(tupla)
print("modificando elementos de la tupla ( tupla[2] = 22 )")
# tupla[2] = 22
print("Al tratar de modificarlas, arroja error")
print("")

print("Conjunto (set)")
# Los conjuntos son "listas" que, al igual que las tuplas, no se pueden modificar, pero si redifinir.
# No se pueden acceder a los elementos individualmente, pero se puede mostrar el conjunto completo
# No permite que se repitan los datos
conjunto = {"Benja", "Sepulveda", 21, 21}
print(conjunto)
print("")

print("Diccionario")
# Los diccionarios son conjuntos de elementos que almacenan una "variable" (que es una clave) y un valor, para acceder a ellos se hace
# mediante el nombre de la variable
diccionario = {
    'nombre' : "Benja" ,
    'apellido' : "Sepulveda",
    'edad' : 21

}
print(diccionario)
print(diccionario['nombre'])
