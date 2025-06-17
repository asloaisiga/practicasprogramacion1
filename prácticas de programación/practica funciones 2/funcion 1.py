"""Ejercicio 1: Análisis de calificaciones
Problema:
Crea un programa que permita ingresar las calificaciones de varios estudiantes y que, mediante
funciones, calcule el promedio general, la calificación más alta y la más baja.
Paso a paso:
1. Definir una función calcular_promedio(lista_notas) que retorne el promedio.
2. Definir funciones nota_mayor(lista) y nota_menor(lista) para obtener el valor máximo y
mínimo.
3. Pedir al usuario la cantidad de estudiantes.
4. Almacenar las calificaciones en una lista.
5. Llamar a las funciones y mostrar resultados."""
def calcular_promedio(lista_notas):
    if not lista_notas:
        return 0
    return sum(lista_notas) / len(lista_notas)
def nota_mayor(lista):
    if not lista:
        return None
    mayor = lista[0]
    for nota in lista:
        if nota > mayor:
            mayor = nota
    return mayor
def nota_menor(lista):
    if not lista:
        return None
    menor = lista[0]
    for nota in lista:
        if nota < menor:
            menor = nota
    return menor
def main():
    try:
        cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
        if cantidad_estudiantes <= 0:
            print("La cantidad de estudiantes debe ser mayor a 0.")
            return
        
        calificaciones = []
        for i in range(cantidad_estudiantes):
            nota = float(input(f"Ingrese la calificación del estudiante {i + 1}: "))
            calificaciones.append(nota)
        
        promedio = calcular_promedio(calificaciones)
        mayor = nota_mayor(calificaciones)
        menor = nota_menor(calificaciones)
        
        print(f"Promedio general: {promedio:.2f}")
        print(f"Calificación más alta: {mayor}")
        print(f"Calificación más baja: {menor}")
    except ValueError:
        print("Por favor, ingrese un número válido.")
main()
