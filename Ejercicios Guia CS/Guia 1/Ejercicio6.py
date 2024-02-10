
#EJERCICIO6

"""
 Implemente un programa en Python que calcule la pendiente y la ordenada al origen de la
 ecuacion de la recta que relaciona la escala de temperatura Fahrenheit con la escala de grados
 Celsius, sabiendo que:

    32 grados Fahrenheit equivalen a 0 grados Celsius

    50 grados Fahrenheit equivalen a 10 grados Celsius

    y = mx + b ; m = (yf-yi)/(xf-xi)

"""

#CONSTANTES

x1 = 32
x2 = 50

y1 = 0
y2 = 10


#PROCESAMIENTO
m = (y2-y1)/(x2-x1)


b =  y1 - m * x1

#SALIDAS

print("La pendiente de la ecuación es: ", m)

print("La ordenada al origen es: ", b)










