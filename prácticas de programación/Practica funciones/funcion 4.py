#funcion que permita obtener el producto de dos numeros enteros
def producto(n1, n2):
    resultado = n1 * n2
    return resultado

#multiplicar 2 numeros
print("Programa para calcular el producto de dos numeros enteros")
n1= int(input("Ingrese el primer numero: "))
n2= int(input("Ingrese el segundo numero: "))
resp=producto(n1, n2)
print(n1, "*", n2, "=", resp)

#obtener la tabla de multiplicar de un numero
print("\nTabla de multiplicar")
num=int(input("Ingrese un numero para obtener su tabla de multiplicar: "))
for i in range(1, 13):
    r= producto(num, i)
    print(num, "*", i, "=", r)