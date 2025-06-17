"""Realice un programa que pida al usuario el nombre o ubicación de un archivo de texto y, 
a continuación añada texto en él hasta que el usuario lo decida.
"""
#solicita al usuario el nombre del archivo
nom=input("Ingrese el nombre del archivo: ")

#encuentra el archivo
try:
    with open(nom, "a", encoding="utf-8") as archivo:
        while True:
            # Solicitar una frase al usuario
            frase = input("Ingrese una frase (o 'salir' para terminar): ")

            # Verificar si el usuario desea salir
            if frase.lower() == 'salir':
                break

            # Escribir la frase en el archivo
            archivo.write(frase + "\n")
            print("Frase guardada correctamente.")
except FileNotFoundError:
    print(f"El archivo '{nom}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
print(f"Todas las frases han sido guardadas en '{nom}'.")