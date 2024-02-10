
#EJERCICIO 1:
"""
Escriba un programa en Python que convierta dıas a segundos y muestre el resultado por
pantalla
"""
#CONSTANTES
horas_dia = 24
minutos_hora = 60
segundos_minutos = 60

#ENTRADAS
print("Ejercicio 1")
#Se asume que se entregan dias enteros y no 1.5 días por ejemplo

dias = int(input("Ingrese la cantidad de días: "))


#PROCESAMIENTO

segundos_hora = segundos_minutos * minutos_hora

segundos_dia = segundos_hora * horas_dia

segundos = segundos_dia * dias

#SALIDAS

print(dias,"dia(s) corresponde(n) a",segundos, "segundos")


