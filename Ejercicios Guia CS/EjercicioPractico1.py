

#Datos promedio de duracion de los cursos de python
otrosCursosMin = 2.5
otrosCursosMax = 7
otrosCursosPromedio = 4
cursoQueEstoyViendo = 1.5

#Diferencias de duracion

diferenciaConMin = 100 - cursoQueEstoyViendo / otrosCursosMin * 100

diferenciaConMax = 100 - cursoQueEstoyViendo * 1000 // otrosCursosMax / 10

diferenciaConPromedio = 100 - cursoQueEstoyViendo / otrosCursosPromedio * 100

print(f'El curso que estoy viendo dura un {diferenciaConMin}% menos que el más rapido')
print(f'El curso que estoy viendo dura un {diferenciaConMax}% menos que el más lento')
print(f'El curso que estoy viendo dura un {diferenciaConPromedio}% menos que el promedio')


#Duracion de crudo (video sin editar)

crudoPromedio = 5
crudoVideoQueVeo = 3.5

#Porcentaje tiempo vacio removido

tiempoVacioPromedio = 100 - otrosCursosPromedio * 1000 // crudoPromedio / 10
tiempoVacioCursoQueVeo = 100 - cursoQueEstoyViendo * 1000 // crudoVideoQueVeo / 10

print(f'Un curso promedio elimina un {tiempoVacioPromedio}% de tiempo vacio')
print(f'El curso que veo eliminó el {tiempoVacioCursoQueVeo}% de tiempo vacio')

#Mostando diferencias si los cursos duran 10 horas

print(f'Ver 10 horas de este curso equivale a ver {otrosCursosPromedio * 100 // cursoQueEstoyViendo / 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {cursoQueEstoyViendo * 100 // otrosCursosPromedio / 10} horas de otros cursos')