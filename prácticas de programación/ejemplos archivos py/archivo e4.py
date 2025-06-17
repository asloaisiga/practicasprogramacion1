#leer con readlines
archi1= open("datos.txt", "r", encoding="utf-8")
lineas=archi1.readlines()
print("El archivo tiene", len(lineas), "líneas")
print("Contenido del archivo: ")
for linea in lineas:
    print(linea, end='')
archi1.close()
