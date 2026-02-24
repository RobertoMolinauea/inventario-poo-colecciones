from modelos.producto import Producto
from servicios.inventario import Inventario

def menu():
    inv = Inventario()

    while True:
        print("\n--- MENÚ INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar por nombre")
        print("5. Mostrar todo")
        print("0. Salir")

        op = input("Opción: ").strip()

        if op == "1":
            pid = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = input("Cantidad: ")
            precio = input("Precio: ")
            inv.agregar(Producto(pid, nombre, cantidad, precio))

        elif op == "2":
            pid = input("ID a eliminar: ")
            inv.eliminar(pid)

        elif op == "3":
            pid = input("ID a actualizar: ")
            cant = input("Nueva cantidad (enter para no cambiar): ").strip()
            prec = input("Nuevo precio (enter para no cambiar): ").strip()

            nueva_cantidad = None if cant == "" else int(cant)
            nuevo_precio = None if prec == "" else float(prec)

            inv.actualizar(pid, nueva_cantidad, nuevo_precio)

        elif op == "4":
            nombre = input("Nombre a buscar: ")
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
