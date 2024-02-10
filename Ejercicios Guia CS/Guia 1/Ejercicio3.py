#EJERCICIO 3

"""
Usando el Teorema de Pitagoras, cree un programa en Python que permita el calculo de
la hipotenusa de un triangulo rectangulo a partir del valor de sus catetos, para cualquier valor
positivo de ellos.

"""

#CONSTANTES

raiz = 1/2

#ENTRADAS

cateto1 = int(input("Ingrese un valor positivo para el cateto 1: "))
cateto2 = int(input("Ingrese un valor positivo para el cateto 2: "))

#PROCESAMIENTO

hipotenusa = (cateto1 * cateto1 + cateto2 * cateto2)**raiz

#SALIDAS
print("La hipotenusa es: ", hipotenusa)