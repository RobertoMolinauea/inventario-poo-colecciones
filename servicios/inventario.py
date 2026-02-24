from modelos.producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.csv"):
        self.archivo = archivo

        # Colecciones
        self.productos = {}      # dict: id -> Producto (búsqueda rápida por ID)
        self.ids = set()         # set: IDs únicos (para validar rápido)
        self.cargar()

    def guardar(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos.values():
                    f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")
        except PermissionError:
            print("No tengo permisos para guardar el archivo.")
        except Exception as e:
            print("Error guardando el archivo:", e)

    def cargar(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for num_linea, linea in enumerate(f, start=1):
                    linea = linea.strip()
                    if not linea:
                        continue

                    partes = linea.split(",")
                    if len(partes) != 4:
                        print(f"Línea {num_linea} dañada (formato). Se ignora.")
                        continue

                    try:
                        p = Producto(partes[0], partes[1], partes[2], partes[3])
                        self.productos[p.get_id()] = p
                        self.ids.add(p.get_id())
                    except ValueError:
                        print(f"Línea {num_linea} dañada (valores). Se ignora.")
        except FileNotFoundError:
            # si no existe, no pasa nada: se crea cuando guardes
            pass
        except PermissionError:
            print("No tengo permisos para leer el archivo.")
        except Exception as e:
            print("Error cargando el archivo:", e)

    def agregar(self, producto):
        pid = producto.get_id()
        if pid in self.ids:
            print("Ese ID ya existe.")
            return

        self.productos[pid] = producto
        self.ids.add(pid)
        self.guardar()
        print("Producto agregado.")

    def eliminar(self, id_producto):
        pid = str(id_producto).strip()
        if pid in self.productos:
            del self.productos[pid]
            self.ids.discard(pid)
            self.guardar()
            print("Producto eliminado.")
        else:
            print("No se encontró ese ID.")

    def actualizar(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        pid = str(id_producto).strip()
        if pid not in self.productos:
            print("No se encontró ese ID.")
            return

        p = self.productos[pid]
        try:
            if nueva_cantidad is not None:
                p.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                p.set_precio(nuevo_precio)
            self.guardar()
            print("Producto actualizado.")
        except ValueError as e:
            print("No se pudo actualizar:", e)

    def buscar_por_nombre(self, nombre):
        nombre = str(nombre).strip().lower()
        encontrados = []  # lista (colección)
        for p in self.productos.values():
            if p.get_nombre().lower() == nombre:
                encontrados.append(p)

        # tupla (colección inmutable) para “demostrar” tuplas
        return tuple(encontrados)

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
            return

        for p in self.productos.values():
            print(p)
