#Ejemplificando funciones definidas por el usuario
def suma(a, b):
    resultado= a + b
    return resultado

#principal
print ("Programa usando funciones en Python")
num1 = int(input("\n Ingrese el primer numero: "))
num2 = int(input("\n Ingrese el segundo numero: "))
print("El resultado de la suma es:", suma(num1, num2))