"""Ejercicio 2: Contador de Líneas
• Problema: Desarrolla un programa que pida al usuario el nombre de un archivo de texto. El
programa deberá leer el archivo y mostrar en pantalla el número total de líneas que contiene.
Debe manejar el error en caso de que el archivo no exista.

• Paso a paso:
1. Solicitar al usuario el nombre del archivo (ej: poema.txt).
2. Usar un bloque try...except para manejar la excepción FileNotFoundError.
3. Dentro del try, abrir el archivo en modo lectura ('r').
4. Utilizar el método readlines() para leer todas las líneas en una lista.
5. Calcular la longitud de la lista (que es igual al número de líneas) y mostrarla.
6. En el bloque except, si el archivo no se encuentra, imprimir un mensaje de error
amigable."""
def contar_lineas_archivo():
    # Paso 1: Solicitar al usuario el nombre del archivo
    nombre= input("Ingrese el nombre del archivo: ")
    
    # Paso 2: Usar un bloque try...except para manejar la excepción FileNotFoundError
    try:
        
        # Paso 3: Abrir el archivo en modo lectura ('r')
        with open(nombre, 'r') as archivo:
            
            # Paso 4: Utilizar el método readlines() para leer todas las líneas en una lista
            lineas = archivo.readlines()
            
            # Paso 5: Calcular la longitud de la lista (que es igual al número de líneas) y mostrarla
            print(f"El archivo '{nombre}' contiene {len(lineas)} líneas.") 
    except FileNotFoundError:
        
        # Paso 6: En el bloque except, si el archivo no se encuentra, imprimir un mensaje de error amigable
        print(f"Lo sentimos, el archivo '{nombre}' no se encontró.")      
if __name__ == "__main__":
    contar_lineas_archivo()
    