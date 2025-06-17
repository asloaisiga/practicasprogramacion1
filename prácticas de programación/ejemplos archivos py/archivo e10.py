"""Realice un programa que pida al usuario el nombre o ubicación de un archivo de texto y,
a continuación de lectura a todo el archivo.
"""
# solicitar nombre del archivo al teclado
archnom=input("Ingrese el nombre del archivo: ")

# Si el archivo no existe, se generará un error. Puede manejarlo con un bloque try-except si es necesario.
# Ejemplo de manejo de errores
try:
    with open(archnom, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
except FileNotFoundError:
    print(f"El archivo '{archnom}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
# Este código solicita al usuario el nombre de un archivo y luego lee su contenido, mostrando el resultado en la consola.
# Si el archivo no existe, se maneja la excepción y se informa al usuario.