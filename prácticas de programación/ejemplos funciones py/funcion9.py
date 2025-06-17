"""Escribe un programa que pregunte al usuario 
un número entero y que mediante una función imprima 
la tabla de multiplicar (del 1 al 10) de dicho número."""
#Bienvenida al usuario
print("Bienvenido al programa que imprime la tabla de multiplicar de un número")

# Definición de la función para imprimir la tabla de multiplicar
def imprimir_tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        
# Solicitar el número al usuario
numero = int(input("Ingrese un número entero para ver su tabla de multiplicar: "))

# Imprimir la tabla de multiplicar
imprimir_tabla_multiplicar(numero)

# Fin del programa
print("Gracias por usar el programa de la tabla de multiplicar.")
print("¡Hasta luego!")