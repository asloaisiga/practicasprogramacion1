"""5. Escriba el programa que contenga una función la cual retorne el factorial de un número capturado por teclado."""
# Bienvenida al usuario
print("Bienvenido al programa que calcula el factorial de un número")
def calcular_factorial(numero):
    if numero < 0:
        return "El factorial no está definido para números negativos."
    elif numero == 0 or numero == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, numero + 1):
            factorial *= i
        return factorial
# Solicitar el número al usuario
numero = int(input("Ingrese un número para calcular su factorial: "))
# Calcular el factorial
factorial = calcular_factorial(numero)
# Mostrar el resultado
print(f"El factorial de {numero} es: {factorial}")
# Fin del programa
print("Gracias por usar el programa del factorial de un número.")
