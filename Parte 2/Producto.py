class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    def obtener_nombre(self):
        return self._nombre

    def obtener_precio(self):
        return self._precio

    def obtener_stock(self):
        return self._stock

    def calcular_precio_final(self):
        return self._precio