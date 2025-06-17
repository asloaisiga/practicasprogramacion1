"""7.Programa para pasar tres argumentos reales a una función que devolverá el menor de ellos. """
# Bienvenida al usuario
print("Bienvenido al programa que encuentra el menor de tres números")
def encontrar_menor(a, b, c):
    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c
    return menor
# Solicitar los tres números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
# Encontrar el menor
menor = encontrar_menor(num1, num2, num3)
# Mostrar el resultado
print(f"El menor de los tres números es: {menor}")
# Fin del programa
print("Gracias por usar el programa que encuentra el menor de tres números.")
