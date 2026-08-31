class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    def ObtenerNombre(self):
        return self._nombre

    def ObtenerPrecio(self):
        return self._precio

    def ObtenerStock(self):
        return self._stock

    def CalcularPrecioFinal(self):
        return self._precio