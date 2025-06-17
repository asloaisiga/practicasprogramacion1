def calcPago(precio, cant):
    return precio * cant
def main():
    productos=[]
    precios=[]
    cantidades=[]
    totales=[]
    resp = "SI"
    while resp.upper() != "NO":
        producto= input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: C$ "))
        cantidad = int(input("Ingrese la cantidad de productos: "))
        total = calcPago(precio, cantidad)
        
        productos.append(producto)
        precios.append(precio)
        cantidades.append(cantidad)
        totales.append(total)
        
        print("Desea ingresar otro producto? (SI/NO)")
        resp = input("Respuesta: ")
    
    print(f'\n{"Factura":^45}')
    print(f'{"Producto":>15} {"Precio":>10} {"Cantidad":>10} {"Total":>10}')
    tam= len(productos)
    for i in range(tam):
        print(f"{productos[i]:15} {precios[i]:10} {cantidades[i]:10} {totales[i]:10}")
        
    monto = sum(totales)
    print(f'{"Total a pagar: C$ ":>42}', monto)
    
main()