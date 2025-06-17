"""Ejercicio 4: Lector de Datos CSV
• Problema: Se proporciona un archivo productos.csv donde cada línea contiene el nombre
de un producto, su precio y la cantidad en stock, separados por comas (ej: Laptop,1200,15).
Escribe un programa que lea este archivo y muestre la información en un formato legible
para el usuario, indicando el nombre, precio y stock de cada producto.
• Paso a paso:
1. Abrir el archivo productos.csv en modo de lectura.
2. Recorrer el archivo línea por línea usando un bucle for.
3. Para cada línea, eliminar el salto de línea final con .strip().
4. Usar el método .split(',') para separar la línea en una lista de tres elementos (nombre,
precio, cantidad).
5. Imprimir los datos de forma ordenada, por ejemplo: Producto: Laptop | Precio: $1200
| Stock: 15 unidades.
6. Cerrar el archivo al finalizar."""
#Crear el archivo productos.csv con algunos datos de ejemplo
with open("productos.csv", "w") as archivo:
    archivo.write("Laptop,1200,15\n")
    archivo.write("Televisor,800,10\n")
    archivo.write("Refrigerador,1500,5\n")
    archivo.write("Smartphone,600,20\n")
    
def lectordatos():
    # Paso 1: Abrir el archivo productos.csv en modo de lectura
    try:
        with open("productos.csv", "r") as archivo:
            # Paso 2: Recorrer el archivo línea por línea usando un bucle for
            for linea in archivo:
                # Paso 3: Para cada línea, eliminar el salto de línea final con .strip()
                linea = linea.strip()
                # Paso 4: Usar el método .split(',') para separar la línea en una lista de tres elementos
                datos = linea.split(',')
                if len(datos) == 3:
                    nombre, precio, cantidad = datos
                    # Paso 5: Imprimir los datos de forma ordenada
                    print(f"Producto: {nombre} | Precio: ${precio} | Stock: {cantidad} unidades.")
                else:
                    print("Formato incorrecto en la línea:", linea)
    except FileNotFoundError:
        print("El archivo 'productos.csv' no se encontró.")
if __name__ == "__main__":
    lectordatos()
    