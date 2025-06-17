#funcion que recibe nombre y apellido por separado y retorna el nombre completo
def nombrecompleto(nom, ape):
    print ("Nombre completo:", nom.title(), ape.title())
def main():
    print("Programa para mostrar el nombre completo")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    nombrecompleto(nombre, apellido)
main()