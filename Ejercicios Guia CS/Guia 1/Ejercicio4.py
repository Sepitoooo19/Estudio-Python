#EJERCICIO 4

"""
Escriba un programa en Python que calcule el ´area de un triangulo mediante la f´ormula de
Heron, siendo a, b y c los lados del tri´angulo.

s = (a + b + c)/2

area = (s * (s-a) * (s-b) * (s-c)) ** (1/2)
"""
#CONSTANTES

raiz = 1/2

#ENTRADAS

a = int(input("Ingrese el valor del lado a: "))
b = int(input("Ingrese el valor del lado b: "))
c = int(input("Ingrese el valor del lado c: "))

#PROCESAMIENTO

s = (a + b + c)/2
area = (s * (s-a) * (s-b) * (s - c))**raiz

#SALIDA

print("El area del triangulo es: ", area)