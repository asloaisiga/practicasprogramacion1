"""Escribir un programa que lea y muestre en pantalla el archivo generado en el ejercicio anterior "archivo e12.py".
"""
#solicitar el nombre del archivo al usuario
nombre_archivo = input("Ingrese el nombre del archivo que contiene los caracteres ASCII: ")

#leer el contenido del archivo
try:
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
# Este código solicita al usuario el nombre de un archivo y luego lee su contenido, mostrando el resultado en la consola.
# Si el archivo no existe, se maneja la excepción y se informa al usuario.
# Fin del programa
