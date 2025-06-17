import re

def tiene_mayus(c):
    """Verifica si la cadena tiene al menos una letra mayúscula."""
    return any(ch.isupper() for ch in c)

def tiene_numero(c):
    """Verifica si la cadena tiene al menos un número."""
    return any(ch.isdigit() for ch in c)

def tiene_caracter_especial(c):
    """Verifica si la cadena tiene al menos un carácter especial."""
    # Definimos como caracteres especiales los que no son alfanuméricos
    return any(not ch.isalnum() for ch in c)

def longitud_minima(c):
    """Verifica si la cadena tiene al menos 8 caracteres."""
    return len(c) >= 8

def main():
    print("Validación de Contraseña")
    print("========================\n")
    password = input("Ingrese su contraseña: ")

    checks = {
        "Mínimo 8 caracteres": longitud_minima(password),
        "Al menos una letra mayúscula": tiene_mayus(password),
        "Al menos un número": tiene_numero(password),
        "Al menos un carácter especial": tiene_caracter_especial(password)
    }

    if all(checks.values()):
        print("\n✅ La contraseña es válida.")
    else:
        print("\n❌ La contraseña NO es válida por los siguientes motivos:")
        for criterio, valido in checks.items():
            if not valido:
                print(f"- {criterio}")

if __name__ == "__main__":
    main()

