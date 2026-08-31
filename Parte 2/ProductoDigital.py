from Producto import Producto

class ProductoDigital(Producto):
    def __init__(self, Nombre, Precio, Stock):
        super().__init__(Nombre, Precio, Stock)

    def CalcularPrecioFinal(self):
        PrecioFinal = self._Precio

        # Si el producto es Digital, aplicar un 15% de descuento
        PrecioFinal = PrecioFinal * 0.85  

        # Si el Stock actual es mayor a 50 unidades, aplicar un 5% de descuento adicional (acumulable).
        if self._Stock > 50:
            PrecioFinal = PrecioFinal * 0.95  

        # Si el precio final es menor a 5.000, el sistema debe imprimir una advertencia de "Revisión de Margen Necesaria".
        if PrecioFinal < 5000:
            print("Revisión de Margen Necesaria")

        return PrecioFinal