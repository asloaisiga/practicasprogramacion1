def calcPago(precio,cant):
    return precio * cant
def main():
    producto=input("Ingrese el nombre del producto: ")
    precio=float(input("Ingrese el precio del producto: C$ "))
    cantidad=int(input("Ingrese la cantidad de productos: "))
    total=calcPago(precio,cantidad)
    print ("Producto:", producto)
    
    print (f'\n{"Factura":^35}')
    print(f'{"Producto":>15}' , f'{"Precio":>10}',f'{"Cantidad":>10}', f'{"Total":>10}')
    print(f"{producto:15} {precio:10} {cantidad:10} {total:10}")

main()
    