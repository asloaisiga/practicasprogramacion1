"""Realice un programa que pida al usuario el nombre de un archivo de texto y, 
a continuación permita almacenar al usuario tantas frases como el usuario desee."""
# Solicitar el nombre del archivo al usuario
nombre_arch= input("Ingrese el nombre del archivo: ")

# Abrir el archivo en modo de escritura (creación)
with open(nombre_arch, "a", encoding="utf-8") as archivo:
    while True:
        # Solicitar una frase al usuario
        frase = input("Ingrese una frase (o 'salir' para terminar): ")
        
        # Verificar si el usuario desea salir
        if frase.lower() == 'salir':
            break
        
        # Escribir la frase en el archivo
        archivo.write(frase + "\n")
        print("Frase guardada correctamente.")
print(f"Todas las frases han sido guardadas en '{nombre_arch}'.")
