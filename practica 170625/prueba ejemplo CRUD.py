import os
#Se importa el modulo os para usar la funcion: os.path.exists(ruta)
ARCHIVO = "estudiantes.txt"

def cargar_estudiantes():
    estudiantes = []
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                codigo, nombre, apellido, carrera =linea.strip().split(",")
                #linea.strip() elimina espacios y saltos de linea (\n) al principio o al final.
                #split(",") divide la cadena en una lista de partes, usando la coma como separador.
                estudiantes.append({
                 "codigo": codigo,
                 "nombre": nombre,
                 "apellido": apellido,
                 "carrera": carrera
                })
    return estudiantes


def guardar_estudiante(estudiantes):
    with open(ARCHIVO, "w") as archivo:
        for est in estudiantes:
            linea = f"{est['codigo']},{est['nombre']},{est['apellido']},{est['carrera']}\n"
            archivo.write(linea)


def crear_estudiante(estudiantes):
    codigo=input("Código del estudiante: ")
    #Verificar si el codigo ya existe
    #La funcion any() devuelve TRUE si al menos un elemento de un iterable es verdadero.
    if any(est['codigo'] == codigo for est in estudiantes):
        print("El código ya existe. Intente con otro.")
        return
    
    nombre = input("Nombre del estudiante: ")
    apellido = input("Apellido del estudiante: ")
    carrera = input("Carrera del estudiante: ")
    
    estudiantes.append({
        "codigo": codigo,
        "nombre": nombre,
        "apellido": apellido,
        "carrera": carrera
    })
    guardar_estudiante(estudiantes)
    print("Estudiante agregado exitosamente.\n")
    
    
def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return
    
    print("\n Lista de estudiantes:")
    for est in estudiantes:
        print(f"Código: {est['codigo']}, Nombre: {est['nombre']}, Apellido: {est['apellido']}, Carrera: {est['carrera']}")
    print()


def actualizar_estudiante(estudiantes):
    codigo= input("Ingrese el codigo del estudiante a actualizar: ")
    for est in estudiantes:
        if est["codigo"]== codigo:
            est["nombre"] = input(f"Nuevo nombre ({est['nombre']}): ") or est["nombre"]
            est["apellido"] = input(f"Nuevo apellido ({est['apellido']}): ") or est["apellido"]
            est["carrera"] = input(f"Nueva carrera ({est['carrera']}): ") or est["carrera"]
            guardar_estudiante(estudiantes)
            print("Estudiante actualizado exitosamente.\n")
            return
    print("Estudiante no encontrado con ese código.\n")

def eliminar_estudiante(estudiantes):
    codigo = input("Ingrese el código del estudiante a eliminar: ")
    for est in estudiantes:
        if est["codigo"] == codigo:
            estudiantes.remove(est)
            guardar_estudiante(estudiantes)
            print("Estudiante eliminado exitosamente.\n")
            return
    print("Estudiante no encontrado con ese código.\n")
    
def menu():
    estudiantes= cargar_estudiantes()
    while True:
        print("========== MENÚ CRUD ESTUDIANTES ==========")
        print("1. Crear estudiante")
        print("2. Mostrar estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            crear_estudiante(estudiantes)
        elif opcion == "2":
            mostrar_estudiantes(estudiantes)
        elif opcion == "3":
            actualizar_estudiante(estudiantes)
        elif opcion == "4":
            eliminar_estudiante(estudiantes)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

#Instruccion para ejecutar el menu
menu()
    
            
        
