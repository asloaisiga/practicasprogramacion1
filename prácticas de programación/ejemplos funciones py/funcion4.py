"""4. Escriba un programa para capturar por teclado el número de horas trabajadas 
y que envíe dicho valor a una función que determine y retorne el valor a pagar, 
considerando que las primeras 160 horas trabajadas serán a $6.5 y el resto de horas a $7.5"""

#bienvenida al usuario
print("Bienvenido al programa que calcula el total a pagar respecto a la cantidad de horas")

def calcular_pago(horas_trabajadas):
    # Tarifas por hora
    tarifa_base = 6.5
    tarifa_extra = 7.5
    horas_base = 160
    
    if horas_trabajadas <= horas_base:
        # Si las horas trabajadas son 160 o menos
        pago_total = horas_trabajadas * tarifa_base
    else:
        # Si hay horas extras
        horas_extras = horas_trabajadas - horas_base
        pago_total = (horas_base * tarifa_base) + (horas_extras * tarifa_extra)
    
    return pago_total


# Solicitar el número de horas trabajadas
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))

# Calcular el pago
pago = calcular_pago(horas_trabajadas)

# Mostrar el resultado
print(f"El valor a pagar por {horas_trabajadas} horas trabajadas es: ${pago:.2f}")