def suma():
    a= int(input("Ingrese el primer numero: "))
    b= int(input("Ingrese el segundo numero: "))
    resultado= a + 2*b
    return resultado
# principal
print ("Programa usando funciones en Python")
resp=suma()
print("El resultado de la suma es:", resp)