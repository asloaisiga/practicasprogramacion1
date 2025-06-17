# Crear o abrir el archivo en modo escritura
with open("ascii.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Tabla de caracteres ASCII (0 - 127)\n")
    archivo.write("----------------------------------\n")
    archivo.write("DECIMAL\tCARÁCTER\n")

    for i in range(128):
        try:
            caracter = chr(i)
            # Mostrar caracteres no imprimibles como texto descriptivo
            if i < 32 or i == 127:
                descripcion = {
                    0: "NUL", 1: "SOH", 2: "STX", 3: "ETX", 4: "EOT",
                    5: "ENQ", 6: "ACK", 7: "BEL", 8: "BS", 9: "TAB",
                    10: "LF", 11: "VT", 12: "FF", 13: "CR", 14: "SO",
                    15: "SI", 16: "DLE", 17: "DC1", 18: "DC2", 19: "DC3",
                    20: "DC4", 21: "NAK", 22: "SYN", 23: "ETB", 24: "CAN",
                    25: "EM", 26: "SUB", 27: "ESC", 28: "FS", 29: "GS",
                    30: "RS", 31: "US", 127: "DEL"
                }.get(i, "CTRL")
                archivo.write(f"{i:>7}\t<{descripcion}>\n")
            else:
                archivo.write(f"{i:>7}\t{caracter}\n")
        except:
            archivo.write(f"{i:>7}\tERROR\n")

print("Archivo 'ascii.txt' creado correctamente.")
