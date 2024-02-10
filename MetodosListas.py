
print("Metodos de Listas")

print("Metodo list(): ") #Crea una lista entrengandole una lista entre corchetes como parametro
lista = list([1,2,3,4,5,6])
print(lista)

print("Metodo len(): ") #Entrega el largo de la lista anterior
print(len(lista))

print("Metodo append(): ") #agrega un elemento a la lista
lista.append(7)
print(lista)

print("Metodo insert(): ") #Inserta un elemento a la lista en un indice especificado
lista.insert(0,0)
print(lista)

print("Metodo extend(): ") #agrega varios elementos a una lsita
lista.extend([2, 3, 4] )
print(lista)

print("Metodo pop(): ") #Elimina elementos en base a un indice, si quieres eliminar el ultimo, se coloca como indice -1
lista.pop(0)
print(lista)

print("Metodo remove(): ") #Remueve en base a un valor
lista.remove(2)
print(lista)

print("Metodo sort(): ") #ordena una lista de menor a mayor, si se le entrega como parametro reverse = True, los ordena al reves
lista.sort()
print(lista)

print("Metodo reverse(): ") #Revierte la lista
lista.reverse()
print(lista)





print("Metodo clear():") #Elimina todos los elementos de la lista
lista.clear()
print(lista)





