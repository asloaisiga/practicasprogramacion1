"""Ejercicio 3: Generador de Listas de Compras
• Problema: Crea un programa que permita al usuario crear una lista de compras. El programa
solicitará al usuario que ingrese productos uno por uno y los guardará en un archivo llamado
compras.txt. El usuario indicará que ha terminado de añadir productos introduciendo la
palabra "fin".
• Paso a paso:
1. Abrir el archivo compras.txt en modo de escritura ('w') para iniciar una nueva lista.
2. Crear un bucle infinito (while True).
3. Dentro del bucle, pedir al usuario que ingrese un producto.
4. Comprobar si la entrada del usuario es "fin". Si lo es, romper el bucle.
5. Si no es "fin", escribir el producto en el archivo, seguido de un salto de línea (\n).
6. Una vez que el bucle termina, cerrar el archivo y notificar al usuario que la lista ha
sido guardada."""
def generar_lista_compras():
    # Paso 1: Abrir el archivo compras.txt en modo de escritura ('w')
    with open("compras.txt", "w") as archivo:
        #Paso 2: Crear un bucle infinito (while True)
        while True:
            # Paso 3: Pedir al usuario que ingrese un producto
            producto = input("Ingrese un producto para la lista de compras (o 'fin' para terminar): ")
            # Paso 4: Comprobar si la entrada del usuario es "fin"
            if producto.lower() == "fin":
                break
            # Paso 5: Si no es "fin", escribir el producto en el archivo
            archivo.write(f"{producto}\n")
        # Paso 6: Una vez que el bucle termina, cerrar el archivo y notificar al usuario
        print("La lista de compras ha sido guardada en 'compras.txt'.")
if __name__ == "__main__":
    generar_lista_compras()
