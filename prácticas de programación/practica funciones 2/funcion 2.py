"""Ejercicio 2: Sistema de conversión de unidades
Problema:
Implementa un programa que, usando funciones, permita convertir entre diferentes unidades de
longitud (metros, kilómetros, pies, pulgadas). El usuario selecciona la conversión deseada y
proporciona el valor.
Paso a paso:
1. Crear funciones como m_km(m), m_pies(m), etc.
2. Mostrar un menú de opciones al usuario.
3. Recibir la opción y el valor.
4. Llamar a la función correspondiente.
5. Mostrar el resultado con 2 decimales."""
#Bienvenida al usuario
print("Bienvenido al sistema de conversión de unidades de longitud.")
# Definición de funciones de conversión
def m_km(m):
    return m / 1000
def m_pies(m):
    return m * 3.28084
def m_pulgadas(m):
    return m * 39.3701
def km_m(km):
    return km * 1000
def km_pies(km):
    return km * 3280.84
def km_pulgadas(km):
    return km * 39370.1
def pies_m(pies):
    return pies / 3.28084
def pies_km(pies):
    return pies / 3280.84
def pies_pulgadas(pies):
    return pies * 12
def pulgadas_m(pulgadas):
    return pulgadas / 39.3701
def pulgadas_km(pulgadas):
    return pulgadas / 39370.1
def pulgadas_pies(pulgadas):
    return pulgadas / 12
# Menú de opciones
def mostrar_menu():
    print("\nSeleccione la conversión deseada:")
    print("1. Metros a Kilómetros")
    print("2. Metros a Pies")
    print("3. Metros a Pulgadas")
    print("4. Kilómetros a Metros")
    print("5. Kilómetros a Pies")
    print("6. Kilómetros a Pulgadas")
    print("7. Pies a Metros")
    print("8. Pies a Kilómetros")
    print("9. Pies a Pulgadas")
    print("10. Pulgadas a Metros")
    print("11. Pulgadas a Kilómetros")
    print("12. Pulgadas a Pies")
def convertir_unidades():
    mostrar_menu()
    try:
        opcion = int(input("Ingrese el número de la opción deseada: "))
        valor = float(input("Ingrese el valor a convertir: "))
        
        if opcion == 1:
            resultado = m_km(valor)
            print(f"{valor} metros son {resultado:.2f} kilómetros.")
        elif opcion == 2:
            resultado = m_pies(valor)
            print(f"{valor} metros son {resultado:.2f} pies.")
        elif opcion == 3:
            resultado = m_pulgadas(valor)
            print(f"{valor} metros son {resultado:.2f} pulgadas.")
        elif opcion == 4:
            resultado = km_m(valor)
            print(f"{valor} kilómetros son {resultado:.2f} metros.")
        elif opcion == 5:
            resultado = km_pies(valor)
            print(f"{valor} kilómetros son {resultado:.2f} pies.")
        elif opcion == 6:
            resultado = km_pulgadas(valor)
            print(f"{valor} kilómetros son {resultado:.2f} pulgadas.")
        elif opcion == 7:
            resultado = pies_m(valor)
            print(f"{valor} pies son {resultado:.2f} metros.")
        elif opcion == 8:
            resultado = pies_km(valor)
            print(f"{valor} pies son {resultado:.2f} kilómetros.")
        elif opcion == 9:
            resultado = pies_pulgadas(valor)
            print(f"{valor} pies son {resultado:.2f} pulgadas.")
        elif opcion == 10:
            resultado = pulgadas_m(valor)
            print(f"{valor} pulgadas son {resultado:.2f} metros.")
        elif opcion == 11:
            resultado = pulgadas_km(valor)
            print(f"{valor} pulgadas son {resultado:.2f} kilómetros.")
        elif opcion == 12:
            resultado = pulgadas_pies(valor)
            print(f"{valor} pulgadas son {resultado:.2f} pies.")
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar un número válido.")
def main():
    while True:
        convertir_unidades()
        continuar = input("¿Desea realizar otra conversión? (s/n): ").strip().lower()
        if continuar != 's':
            print("Gracias por usar el sistema de conversión de unidades. ¡Hasta luego!")
            break
main()
# Este código implementa un sistema de conversión de unidades de longitud con funciones específicas para cada tipo de conversión.
"""El usuario puede seleccionar la conversión deseada a través de un menú y el programa realiza la conversión mostrando 
el resultado con dos decimales."""


