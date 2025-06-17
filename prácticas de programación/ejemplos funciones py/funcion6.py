"""6. Escribir el programa que tenga una función, esta devuelva el área de un círculo cuyo radio se le suministra como argumento."""
"""Nota: NO usar la función de área de un círculo de la librería math,
sino que debe ser una función definida por el usuario."""
# Bienvenida al usuario
print("Bienvenido al programa que calcula el área de un círculo")
def calcular_area_circulo(radio):
    # Definición de la constante pi
    pi = 3.141592653589793
    # Cálculo del área del círculo
    area = pi * (radio ** 2)
    return area
# Solicitar el radio al usuario
radio = float(input("Ingrese el radio del círculo: "))
# Calcular el área
area = calcular_area_circulo(radio)
# Mostrar el resultado
print(f"El área del círculo con radio {radio} es: {area:.2f}")
# Fin del programa
print("Gracias por usar el programa del área de un círculo.")
