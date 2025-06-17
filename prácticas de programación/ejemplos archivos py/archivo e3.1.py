#leer el contenido del archivo de texto linea a linea
archi1=open("datos.txt", "r", encoding="utf-8")
for linea in archi1:
    print(linea, end='')
archi1.close()
