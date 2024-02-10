#EJERCICIO5


"""

 Construya un programa en Python que calcule el numero de atomos contenidos en el cuerpo
 de una persona cualquiera y el porcentaje que estos ocupan en el universo. Se sabe que el
 numero de atomos en una persona de 70 kilogramos es de 7 * 10^27 y que el numero de atomos
 en el universo es de 1 * 10^81.


"""


#CONSTANTES

atomosUniverso = 1 * 10 ** 81

#ENTRADAS

pesoPersona = int(input("Ingrese el peso de la persona: "))


#PROCEDIMIENTO

atomosEnPersona = (pesoPersona * 10**27) / 70

porcentajeEnUniverso = (atomosEnPersona / atomosUniverso) * 100


#SALIDAS
print("La cantidad de atomos de una persona de",pesoPersona,"kilogramos es de",atomosEnPersona,
      "y el porcentaje que ocupa en el universo es de",porcentajeEnUniverso,"%")


