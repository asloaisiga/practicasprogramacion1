"""3. Escribir un programa que permita ingresar los salarios de una cantidad indicada de empleados, 
debe presentar al final el total que se debe pagar a cada empleado y el descuento de renta considerando
que es del 10% sobre cada salario. Utiliza una función para el cálculo del descuento."""

#bienvenida al usuario
print("Bienvenido al programa que calcula el descuento de renta sobre el salario de n empleados")

#definicion de funciones

def desc_renta(salario_base):
    #calculo del porcentaje
    descrenta = salario_base * 0.10

    #calculo final del final total con descuento
    totalcondesc = salario_base - descrenta
    return descrenta, totalcondesc
    
#solicitar el numero de vendedores
numempleados=int(input("Ingresa el numero de empleados en esta empresa: "))

#proceso de cada vendedor
for i in range (numempleados):
    print(f"\nEmpleado {i + 1}:")
    salario_base=float(input("Ingrese el salario del empleado: C$ "))
    
    descuento, total = desc_renta(salario_base)
    print(f"Descuento de renta: C$ {descuento:.2f}")
    print(f"Salario total con descuento: C$ {total:.2f}")