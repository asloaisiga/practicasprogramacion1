"""8. Crear una función que reciba como argumento el importe de una compra y devuelva la cantidad final a pagar,
teniendo en cuenta que los descuentos son del 5% cuando se compra más de 300 €, del 10% cuando se compra más de 500 €
y del 12% para cantidades mayores de 500 €, escribe un programa que pregunte al usuario la cantidad comprada
y le indique el importe a pagar."""
# Bienvenida al usuario
print("Bienvenido al programa que calcula el importe final a pagar por una compra")
def calcular_importe_final(compra):
    if compra > 500:
        descuento = 0.12
    elif compra > 300:
        descuento = 0.10
    elif compra > 100:
        descuento = 0.05
    else:
        descuento = 0.0
    
    importe_final = compra * (1 - descuento)
    return importe_final
# Solicitar el importe de la compra al usuario
compra = float(input("Ingrese el importe de la compra: € "))
# Calcular el importe final
importe_final = calcular_importe_final(compra)
# Mostrar el resultado
print(f"El importe final a pagar por la compra de €{compra:.2f} es: €{importe_final:.2f}")
# Fin del programa
print("Gracias por usar el programa de cálculo de importe final a pagar.")
