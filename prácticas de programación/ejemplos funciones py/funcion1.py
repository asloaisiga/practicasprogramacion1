"""1.Crear un programa que dado un monto para presupuesto anual de una fábrica
calcule el porcentaje de dinero que le corresponde a cada departamento.
El cálculo se realizará en una función que recibe como argumento el monto.
Recursos Humanos	50%
Manufactura			25%
Empaquetado		    15%
Publicidad			10%
"""
#Bienvenida al usuario
print("Bienvenido al programa que calcula el presupuesto anual de una fabrica por departamento")
print("=======================================================================================")

#definicion de las funciones

def calcular_presupuesto(monto):
    # Porcentajes de cada departamento
    porcentajes = {
        "Recursos Humanos": 0.50,
        "Manufactura": 0.25,
        "Empaquetado": 0.15,
        "Publicidad": 0.10
    }
    
# Definición del calculo de presupuesto correspondiente para cada departamento
    presupuesto_departamentos = {departamento: monto * porcentaje for departamento, porcentaje in porcentajes.items()}
    
    return presupuesto_departamentos

# Ejemplo de uso
monto_anual = float(input("Ingrese el monto del presupuesto anual: "))

presupuesto = calcular_presupuesto(monto_anual)
# Mostrar resultados
print("=======================================================================")
print("El monto correcpondiente del presupuesto anual según departamento es: ")
print("=======================================================================")
for departamento, cantidad in presupuesto.items():
    print(f"{departamento}: ${cantidad:.2f}")
