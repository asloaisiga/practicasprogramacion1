""" Ejercicio 9: Registro de eventos en un archivo de log
Registro de eventos en un archivo de log: Diseña un programa que simule un sistema de registro de eventos. 
Debe agregar una línea a un archivo “log.txt” cada vez que se ejecute, 
incluyendo la fecha y hora actuales y un mensaje de evento proporcionado por el usuario."""

import os # Importamos el módulo os para trabajar con archivos y directorios
EVENTOS= "log.txt" #variable para almacenar el archivo de log
from datetime import datetime # Se importa datetime para trabajar con fechas y horas

# Verificamos si el archivo de log existe, si no, lo creamos
if not os.path.exists(EVENTOS):
    with open(EVENTOS, "w") as archivo_log:
        archivo_log.write("Registro de eventos iniciado.\n")  # Escribimos una línea inicial en el archivo
        print(f"Archivo {EVENTOS} creado exitosamente.")
else:
    print(f"El archivo {EVENTOS} ya existe. Se añadirá a él.")

# Se crea una funcion para registrar eventos en un archivo de log
# La funcion recibe un mensaje y lo escribe en el archivo junto con la fecha y hora actuales
def registrar_evento(mensaje):
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(EVENTOS, "a") as archivo_log:
        archivo_log.write(f"{fecha_hora} - {mensaje}\n")

# La funcion eventoexitoso solicita al usuario un mensaje de evento
# y lo registra en el archivo de log hasta que el usuario decida salir
# Si el usuario ingresa 'salir', se termina el registro de eventos
def eventoexitoso():
    while True:
        mensaje = input("Ingrese un mensaje de evento (o 'salir' para terminar): ")
        if mensaje.lower() == 'salir':
            print("Saliendo del registro de eventos.")
            break
        registrar_evento(mensaje)
        print("Evento registrado exitosamente.")
        
eventoexitoso()

