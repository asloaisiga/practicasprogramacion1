"""Ejercicio 1: Diario Personal
• Problema: Escribe un programa que funcione como un diario simple. Cada vez que se
ejecute, debe solicitar al usuario una entrada de texto y la guardará, junto con la fecha y hora
actual, en un archivo llamado diario.txt. Cada nueva entrada debe añadirse al final del
archivo sin borrar las anteriores.
• Paso a paso:
1. Importar el módulo datetime para obtener la fecha y hora.
2. Solicitar al usuario que ingrese el texto para su entrada del diario.
3. Abrir el archivo diario.txt en modo de adición ('a').
4. Escribir la fecha y hora actual, seguida de la entrada del usuario. Asegurarse de
añadir un salto de línea para separar las entradas.
5. Cerrar el archivo.
6. Mostrar un mensaje de confirmación al usuario.
"""
from datetime import datetime
def escribir_diario():
    #Paso 1: Importar el modulo datetime
    fecha_hora_actual=datetime.now()
    #Paso 2: Solicitar al usuario que ingrese el texto para su entrada del diario
    entradauser=input("Ingrese su texto al diario: ")
    #Paso 3: Abrir el archivo diario.txt en modo de adición ('a')
    with open("diario.txt", "a") as diario:
        #Paso 4: Escribir la fecha y hora actual, seguida de la entrada del usuario
        diario.write(f"{fecha_hora_actual.strftime('%Y-%m-%d %H:%M:%S')} - {entradauser}\n")
    #Paso 5: Cerrar el archivo (con 'with' se cierra automáticamente)
    #Paso 6: Mostrar un mensaje de confirmación al usuario
    print("Entrada guardada en el diario con éxito.")
if __name__ == "__main__":
    escribir_diario()
    
        