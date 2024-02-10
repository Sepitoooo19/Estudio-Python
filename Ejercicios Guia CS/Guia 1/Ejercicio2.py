
#EJERCICIO 2

"""
Construya un programa en Python que convierta un n´umero dado de segundos a horas,
minutos y segundos.

Ejemplo: 3661 segundos equivalen a una hora, un minuto y un segundo.

"""
#CONSTANTES

horas = 24
minutos = 60
segundos = 60

#ENTRADAS

segundos_dados = int(input("Ingrese la cantidad de segundos: "))

#PROCESAMIENTO

horasEnSegundos = segundos_dados // 3600

horasTotales = horasEnSegundos * 3600

segundosRestantes = segundos_dados - horasTotales

minutosEnSegundos = segundosRestantes // 60

minutosTotales = minutosEnSegundos * 60

segundosRestantes2 = segundosRestantes - minutosTotales

#SALIDAS
print(segundos_dados, "segundos tiene:", horasEnSegundos, "horas,", minutosEnSegundos, "minutos y", segundosRestantes2, "segundos" )

