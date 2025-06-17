#Leer el contenido del archivo de texto línea a línea
archi1 = open("datos.txt", "r", encoding="utf-8")  # Modo lectura
linea = archi1.readline()  # Leer la primera línea
while linea != '':
    print(linea, end='')
    linea = archi1.readline()  # Leer la siguiente línea
archi1.close()

