
print("Conjunto creado")
conjunto = set(["Dato1", "Dato2"])
print(conjunto)

print("")

print("Conjunto con una tupla dentro")
conjunto1 = frozenset(["Dato1", "Dato2", ("Dato1", "Dato2")])
print(conjunto)

print("Para poder meter un conjunto dentro de otro conjunto se debe usar frozenset")
conjunto2 = {conjunto1, "Dato1", "Dato2" }
print(conjunto2)
print("")


#TEORIA DE CONJUNTOS
print("Nuevos conjuntos creados")
conjunto1 =  {1,3,5,7}
conjunto2 = {1,3,7}
print(conjunto1)
print(conjunto2)
print("Para ver si un conjunto es subconjunto de otro, en este caso si conjunto2 es subconjunto de conjunto1, se usa issubset()")
resultado = conjunto2.issubset(conjunto1)
print(resultado)
print("Para ver si un conjunto es superconjunto de otro, en este caso si conjunto1 es superconjunto de conjunto2, se usa issuperset()")
resultado2 = conjunto1.issuperset(conjunto2)
print(resultado2)

print("Para verificar si hay algun elemento en comun entre los conjuntos, se usa isdisjoint(), si es true, "
      "es porque todos los elementos son distintos, si es false, es porque hay almenos 1 elemento igual")
resultado3 = conjunto2.isdisjoint(conjunto1)
print(resultado3)
