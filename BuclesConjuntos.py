

print("Lista creada")
animales = ["Perro", "Gato", "Loro", "Cocodrilo", "pez"]
print(animales)
print("")

print("Recorriendo la lista creada")
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')

print("\n\n")

print("2da lista creada")

numeros = [1,2,3,4]

print(numeros)

for numero in numeros:
    resultado = numero * 2
    print(f'El resultado de {numero} multiplicado por 2 es {resultado}')

print("\n\n")

print("Para recorrer 2 listas a la vez, dejando de lado los ciclos anidados, se puede utilizar la funcion zip()")

for numero,animal in zip(numeros,animales):
    print(f'Recorriendo lista 1: {numero}')
    print(f'Recorriendo lista 2: {animal}')


print("\n\n")

#Forma no optima de recorrer una lista con su indice

#for num in range(len(numeros)):
 #   print(numeros[num])



#Forma correcta de recorrer una lista con su indice
print("Usando enumerate")
for num in enumerate(numeros):
    indice = num[0]
    numero = num[1]
    print(f'el indice es {indice} y el numero es {numero}')
print("")

print("Usando else al final del for")
for num in numeros:
    print(f'Ejecutando el ultimo bucle, valor actual: {num}')

else:
    print("El bucle terminó")

