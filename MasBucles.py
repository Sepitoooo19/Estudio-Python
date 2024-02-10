
print("Lista creada")
frutas = ["Manzana", "Uva", "Platano", "Naranja", "Pera", "Melon", "Durazon", "Frutilla"]
cadena = "Benjamin"

for fruta in frutas:
    if fruta == "Melon":
        continue; #Sirve para continuar el bucle si es que se cumple una condicion
    print(f'Me voy a comer una {fruta}')
print("\n\n")

#Break sirve para terminar todos los bucles si se cumple una condicion, en caso de que haya un else, tampoco se ejecuta
for fruta in frutas:
    if fruta == "Platano":
        print("No como más")
        break;

    print(f'Me voy a comer una {fruta}')

print("\n")
print("La cadena es: ", cadena)

for letra in cadena:
    print(letra)

print("\n\n")



print("Nueva lista creada")
numeros = [1,2,3,4,5]
print("Ciclos for en una sola linea (numerosPorDos = [x * 2 for x in numeros])")

numerosPorDos = [x * 2 for x in numeros]
print(numerosPorDos)


