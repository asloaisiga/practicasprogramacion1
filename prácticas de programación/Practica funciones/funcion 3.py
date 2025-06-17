#crea una funcion que calcule el promedio de tres notas (de 0 a 100)
def promediogeneral(nota1, nota2, nota3):
    promediogeneral = (nota1+nota2+nota3)/3
    return promediogeneral
# principal
print("Programa para calcular el promedio de tres notas")
nota1 = int(input("Ingrese la primera nota (0-100): "))
nota2 = int(input("Ingrese la segunda nota (0-100): "))
nota3 = int(input("Ingrese la tercera nota (0-100): "))
# Llamada a la función y mostrar el resultado
resultado = promediogeneral(nota1, nota2, nota3)
print("El promedio de las notas es:", resultado)

