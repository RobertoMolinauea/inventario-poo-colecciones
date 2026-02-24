from modelos.producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.csv"):
        self.archivo = archivo
        self.productos = {}  # diccionario: id -> Producto
        self.cargar()

    def guardar(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            for p in self.productos.values():
                f.write(f"{p.id},{p.nombre},{p.cantidad},{p.precio}\n")

    def cargar(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue
                    partes = linea.split(",")
                    if len(partes) != 4:
                        continue
                    p = Producto(partes[0], partes[1], int(partes[2]), float(partes[3]))
                    self.productos[p.id] = p
        except FileNotFoundError:
            # si no existe, se creará al guardar
            pass

    def agregar(self, producto):
        if producto.id in self.productos:
            print("Ese ID ya existe.")
            return
        self.productos[producto.id] = producto
        self.guardar()
        print("Producto agregado.")

    def eliminar(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar()
            print("Producto eliminado.")
        else:
            print("No se encontró ese ID.")

    def actualizar(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto not in self.productos:
            print("No se encontró ese ID.")
            return

        p = self.productos[id_producto]

        if nueva_cantidad is not None:
            p.cantidad = int(nueva_cantidad)
        if nuevo_precio is not None:
            p.precio = float(nuevo_precio)

        self.guardar()
        print("Producto actualizado.")

    def buscar_por_nombre(self, nombre):
        nombre = nombre.strip().lower()
        encontrados = []
        for p in self.productos.values():
            if p.nombre.lower() == nombre:
                encontrados.append(p)
        return encontrados

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
            return
        for p in self.productos.values():
            print(p)
