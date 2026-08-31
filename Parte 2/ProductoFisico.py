from producto import Producto

class ProductoFisico(Producto):
    def __init__(self, nombre, precio, stock):
        super().__init__(nombre, precio, stock)

    def CalcularPrecioFinal(self):
        PrecioFinal = self._precio

        # Si el Stock actual es mayor a 50 unidades, aplicar un 5% de descuento
        if self._stock > 50:
            PrecioFinal = PrecioFinal * 0.95  

        # Si el precio final es menor a 5.000, el sistema debe imprimir una advertencia de "Revisión de Margen Necesaria"
        if PrecioFinal < 5000:
            print("Revisión de Margen Necesaria")

        return PrecioFinal