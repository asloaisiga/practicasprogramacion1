#solicitando datos al usuario:

nombre= input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
salario = input("Ingrese su salario: C$ ")

#Formatear los datos en una linea
linea= f"{nombre},{apellido},{edad},{salario}\n"

#guardar los datos en un archivo
with open("datos_usuarios.txt", "a", encoding="utf-8") as archivo:
    archivo.write(linea)
    
print("Datos guardados correctamente.")