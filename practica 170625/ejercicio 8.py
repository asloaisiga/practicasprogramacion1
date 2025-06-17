"""Ejercicio 8: Filtrado de líneas que contienen una palabra específica: Escribe un programa que lea un archivo “libro.txt” 
y cree un nuevo archivo “filtrado.txt” que solo contenga las líneas que tienen una palabra específica 
proporcionada por el usuario."""

# Importamos el módulo os para trabajar con archivos y directorios
import os
# Verificamos si el archivo libro.txt existe, si no, lo creamos
if not os.path.exists("libro.txt"):
    with open("libro.txt", "w", encoding='utf-8') as archivo_libro:
        archivo_libro.write("Este es un ejemplo de libro.\n")
        archivo_libro.write("Contiene varias líneas de texto.\n")
        archivo_libro.write("Puedes buscar palabras específicas en él.\n")
        print("Archivo 'libro.txt' creado exitosamente.")
else:
    print("El archivo 'libro.txt' ya existe. Se procederá a filtrar las líneas.")
# Solicita al usuario una palabra para filtrar las líneas del archivo libro.txt
# Luego, crea un nuevo archivo filtrado.txt con las líneas que contienen esa palabra.
def filtrar_lineas(palabra):
    with open("libro.txt", "r", encoding='utf-8') as archivo_libro:
        lineas = archivo_libro.readlines()  # Leemos todas las líneas del archivo

    with open("filtrado.txt", "w", encoding='utf-8') as archivo_filtrado:
        for linea in lineas:
            if palabra in linea:  # Verificamos si la palabra está en la línea
                archivo_filtrado.write(linea)  # Escribimos la línea en el nuevo archivo

    print(f"Filtrado completado. Las líneas que contienen '{palabra}' se han guardado en 'filtrado.txt'.")

def main():
    palabra = input("Ingrese una palabra para filtrar las líneas del archivo 'libro.txt': ")
    filtrar_lineas(palabra)
main()