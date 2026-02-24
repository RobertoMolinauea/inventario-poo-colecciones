class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = str(id_producto).strip()
        self.nombre = str(nombre).strip()
        self.cantidad = int(cantidad)
        self.precio = float(precio)

    def __str__(self):
        return f"{self.id} - {self.nombre} | cant: {self.cantidad} | $ {self.precio:.2f}"
