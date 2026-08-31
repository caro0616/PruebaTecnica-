from ProductoFisico import ProductoFisico
from ProductoDigital import ProductoDigital

ListaProductos = []

def MostrarMenu():
    print("\n--- Menú de Inventario EmasT ---")
    print("1. Agregar producto fisico")
    print("2. Agregar producto digital")
    print("3. Ver lista de productos con su precio final")
    print("4. Salir")

def AgregarProductoFisico():
    Nombre = input("Nombre del producto: ")
    Precio = float(input("Precio: "))
    Stock = int(input("Stock: "))
    NuevoProducto = ProductoFisico(Nombre, Precio, Stock)
    ListaProductos.append(NuevoProducto)
    print("Producto físico agregado")

def AgregarProductoDigital():
    Nombre = input("Nombre del producto: ")
    Precio = float(input("Precio: "))
    Stock = int(input("Stock: "))
    NuevoProducto = ProductoDigital(Nombre, Precio, Stock)
    ListaProductos.append(NuevoProducto)
    print("Producto digital agregado")

def VerProductos():
    if len(ListaProductos) == 0:
        print("Todavía no hay productos")
        return

    for Producto in ListaProductos:
        PrecioFinal = Producto.CalcularPrecioFinal()
        print(f"{Producto._Nombre} - Precio final: {PrecioFinal}")

while True:
    MostrarMenu()
    Opcion = input("Elegí una opción: ")

    if Opcion == "1":
        AgregarProductoFisico()
    elif Opcion == "2":
        AgregarProductoDigital()
    elif Opcion == "3":
        VerProductos()
    elif Opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción inválida, intentá de nuevo.")