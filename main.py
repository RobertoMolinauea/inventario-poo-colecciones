from modelos.producto import Producto
from servicios.inventario import Inventario

def menu():
    inv = Inventario()

    while True:
        print("\n--- MENÚ INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio")
        print("4. Buscar por nombre")
        print("5. Mostrar todo")
        print("0. Salir")

        op = input("Opción: ").strip()

        if op == "1":
            try:
                pid = input("ID: ").strip()
                nombre = input("Nombre: ").strip()
                cantidad = input("Cantidad: ").strip()
                precio = input("Precio: ").strip()
                inv.agregar(Producto(pid, nombre, cantidad, precio))
            except Exception as e:
                print("No se pudo agregar:", e)

        elif op == "2":
            pid = input("ID a eliminar: ").strip()
            inv.eliminar(pid)

        elif op == "3":
            pid = input("ID a actualizar: ").strip()
            cant = input("Nueva cantidad (enter para no cambiar): ").strip()
            prec = input("Nuevo precio (enter para no cambiar): ").strip()

            nueva_cantidad = None if cant == "" else cant
            nuevo_precio = None if prec == "" else prec

            inv.actualizar(pid, nueva_cantidad, nuevo_precio)

        elif op == "4":
            nombre = input("Nombre a buscar: ").strip()
            encontrados = inv.buscar_por_nombre(nombre)
            if not encontrados:
                print("No se encontró.")
            else:
                for p in encontrados:
                    print(p)

        elif op == "5":
            inv.mostrar_todos()

        elif op == "0":
            print("Listo, saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
