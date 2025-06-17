#Programa principal
import funcion4

print("Calcula las operaciones básicas con módulo")
n1=int(input("Ingresa un número: "))
n2=int(input("Ingresa otro número: "))

print("=============================================")
print("El producto de", n1, "por", n2, "es:" , funcion4.prod(n1,n2))

resp= funcion4.resta(n1, n2)

print("==============================================")
print("La diferencia de", n1, "menos", n2, "es:", resp)

from funcion4 import suma
print("=============================================")
print("La suma es: ", suma(n1,n2))

print("==============================================")
import funcion4 as md
print("El cociente resultante es:", md.division(n1,n2))

