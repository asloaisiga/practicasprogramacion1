"""Ejercicio 3: Validación de contraseña
Problema:
Desarrolla un programa que valide una contraseña según los siguientes criterios: mínimo 8
caracteres, al menos una mayúscula, un número y un carácter especial. Usar funciones para
cada validación.
Paso a paso:
1. Crear funciones como tiene_mayus(c), tiene_numero(c), etc.
2. Usar all() para evaluar si todas devuelven True.
3. Solicitar la contraseña al usuario.
4. Indicar si es válida o no, y por qué."""
#Bienvenida al usuario
print("Bienvenido al sistema de validación de contraseñas.")
print("Al ingresar, la contraseña debe cumplir con los siguientes criterios:")
print("- Mínimo 8 caracteres.")
print("- Al menos una letra mayúscula.")
print("- Al menos una letra minúscula.")
print("- Al menos un número.")
print("- Al menos un carácter especial.")
# Definición de funciones de validación
#usar all() para evaluar si todas las funciones devuelven True
def tiene_mayus(c):
    return any(char.isupper() for char in c)
def tiene_minus(c):
    return any(char.islower() for char in c)
def tiene_numero(c):
    return any(char.isdigit() for char in c)
def tiene_caracter_especial(c):
    caracteres_especiales = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"
    return any(char in caracteres_especiales for char in c)
def es_valida_contrasena(contrasena):
    return (len(contrasena) >= 8 and
            tiene_mayus(contrasena) and
            tiene_minus(contrasena) and
            tiene_numero(contrasena) and
            tiene_caracter_especial(contrasena))
def validar_contrasena():
    contrasena = input("Ingrese la contraseña a validar: ")
    
    if es_valida_contrasena(contrasena):
        print("La contraseña es válida.")
    else:
        print("La contraseña no es válida.")
        if len(contrasena) < 8:
            print("- Debe tener al menos 8 caracteres.")
        if not tiene_mayus(contrasena):
            print("- Debe contener al menos una letra mayúscula.")
        if not tiene_minus(contrasena):
            print("- Debe contener al menos una letra minúscula.")
        if not tiene_numero(contrasena):
            print("- Debe contener al menos un número.")
        if not tiene_caracter_especial(contrasena):
            print("- Debe contener al menos un carácter especial.")
    #si la contraseña es invalida, se debe volver a solicitar al usuario que ingrese una contraseña
    while not es_valida_contrasena(contrasena):
        contrasena = input("Ingrese una contraseña válida: ")
        if es_valida_contrasena(contrasena):
            print("La contraseña es válida.")
            break
        else:
            print("La contraseña no es válida. Por favor, inténtelo de nuevo.")
                  
# Función principal para ejecutar el programa
def main():
    validar_contrasena()
main()
