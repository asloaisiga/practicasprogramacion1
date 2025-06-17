#trabajando con archivos de texto en python
#1. abrir el archivo en modo creacion
#ejemplo, solicitando el nombre del archivo al user
ruta=input("Ingrese el nombre del archivo: ")
archivo1=open(ruta, "a", encoding="utf-8")
#archivo1.write("Primera linea \n")
archivo1.write("Segunda línea \n")
archivo1.write("Tercera línea \n")
archivo1.write(input("Ingrese una línea de texto: ") + "\n")
archivo1.close()
