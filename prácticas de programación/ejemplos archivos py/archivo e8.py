#eliminar lineas del archivo
#abrir el archivo y leer las lineas
with open("datos.txt","r", encoding="utf-8") as archivo1:
    lineas = archivo1.readlines()

#filtrar las lineas que no contienen "segunda linea"
lineas_filtradas = [linea for linea in lineas if linea.strip() != "Segunda linea"]

#sobreescribir el archivo con las lineas filtradas
with open("datos.txt", "w", encoding="utf-8") as archivo1:
    archivo1.writelines(lineas_filtradas)
    