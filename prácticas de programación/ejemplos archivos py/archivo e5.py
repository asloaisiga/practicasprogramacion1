#ejemplo con r+
archi1=open("datos.txt","r+", encoding="utf-8")
contenido=archi1.read()
print(contenido)
archi1.write("\nNueva línea añadida al final del archivo.")
archi1.write("\nOtra línea añadida al final del archivo.")
archi1.close()
