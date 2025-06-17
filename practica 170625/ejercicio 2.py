"""Ejercicio 2: Contador de palabras en un archivo: Crea un programa que lea un archivo llamado “articulo.txt” 
y cuente cuántas veces aparece una palabra específica proporcionada por el usuario."""

import os
ARTICULO = "articulo.txt"

#Crear el archivo articulo.txt si no existe
if not os.path.exists(ARTICULO):
    with open(ARTICULO, "w", encoding="utf-8") as archivo:
        archivo.write("Este es un artículo de ejemplo.\n")
        archivo.write("Contiene varias líneas de texto.\n")
        archivo.write("Puedes buscar palabras específicas en él.\n")
        print(f"Archivo '{ARTICULO}' creado exitosamente.")
else:
    print(f"El archivo '{ARTICULO}' ya existe. Se procederá a contar las palabras.")
    
# Función para contar cuántas veces aparece una palabra específica en un archivo
def contar_palabra(articulo, palabra_buscada):
    try:
        with open(articulo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().lower()
            palabra_buscada = palabra_buscada.lower()
            palabras = contenido.split()
            contador = palabras.count(palabra_buscada)

            print(f"La palabra '{palabra_buscada}' aparece {contador} veces en el archivo.")
    except FileNotFoundError:
        print(f"El archivo '{articulo}' no fue encontrado.")

palabra_usuario = input("Ingrese la palabra que desea buscar: ")
contar_palabra(ARTICULO, palabra_usuario)

