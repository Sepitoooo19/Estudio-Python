

edad = int(input("Ingrese su edad: "))

# Los if-else son condicionales que deciden el flujo del programa, por decirlo de alguna manera
# se verifica si se cumple la condicion, si es asi, realiza algo, si no, hace otra cosa


if edad >= 18:
    print("Eres mayor de edad")

elif edad < 0:
    print("No has nacido aun")

else:
    print("Eres menor de edad")

print("Tu edad es", edad)