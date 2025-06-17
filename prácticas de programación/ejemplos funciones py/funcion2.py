"""2. Una compañía de seguros tiene contratados a n vendedores. Cada uno hace tres ventas a la semana.
Su política de pagos es que un vendedor recibe un sueldo base, y un 10% extra por comisiones de sus ventas.
El gerente de su compañía desea saber cuánto dinero obtendrá en la semana cada vendedor por concepto de comisiones
por las tres ventas realizadas, y cuanto tomando en cuenta su sueldo base y sus comisiones.
Utilice una función para calcular la comisión por las tres ventas realizadas."""

#bienvenida al usuario
print("Bienvenido al programa que calcula la comisión de n vendedores por 3 ventas realizadas")

#definicion de funciones

def calcular_comisiones(sueldo_base, precio_venta):
    # Número de ventas por semana
    ventas_por_semana = 3
    
    # Cálculo de la comisión (10% del precio de la venta)
    comision_por_venta = precio_venta * 0.10
    comision_total = comision_por_venta * ventas_por_semana
    
    # Cálculo del total a recibir (sueldo base + comisiones)
    total_semanal = sueldo_base + comision_total
    
    return comision_total, total_semanal

# Solicitar el número de vendedores

num_vendedores = int(input("Ingrese el número de vendedores en la compañía: "))

# Procesar cada vendedor
for i in range(num_vendedores):
    print(f"\nVendedor {i + 1}:")
    sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))
    precio_venta = float(input("Ingrese el precio de cada venta: "))
    
    comision, total = calcular_comisiones(sueldo_base, precio_venta)
    
    # Mostrar resultados
    print(f"Comisión total por ventas en la semana: ${comision:.2f}")
    print(f"Total a recibir en la semana (sueldo base + comisiones): ${total:.2f}")