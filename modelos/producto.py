class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = str(id_producto).strip()
        self.set_nombre(nombre)
        self.set_cantidad(cantidad)
        self.set_precio(precio)

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        nombre = str(nombre).strip()
        if nombre == "":
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        cantidad = int(cantidad)
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self._cantidad = cantidad

    def set_precio(self, precio):
        precio = float(precio)
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = precio

    def __str__(self):
        return f"{self._id} - {self._nombre} | cant: {self._cantidad} | $ {self._precio:.2f}"
