#Identicando archivos de texto en python 
#Creando el archivo datos.txt

archi1=open("datos.txt","w", encoding="utf-8") #Modo escritura

archi1.write("Primera línea  \n")
archi1.write("Segunda línea  \n")
archi1.write("Tercera línea  \n")
archi1.write("Cuarta línea  \n")
archi1.write("Fin del archivo \n")
archi1.close()

print("Fin del programa")

