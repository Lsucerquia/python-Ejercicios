class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

def Mostrar_menu():
    print("Sistema de inventario")
    print("1. Agregar producto")
    print("2. Mostrar producto")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")

inventario = []

while True:
    Mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "6":
        print("Saliendo del programa")
        break

    if opcion == "1":
        nombre = input("Ingresa el nombre del producto: ")
        try:
            cantidad = int(input("Ingresa la cantidad: "))
            precio = float(input("Ingresa el precio: "))
            producto = Producto(nombre, cantidad, precio)
            inventario.append(producto)
            print("Producto agregado")
            input("\nPresiona Enter para regresar al menú...")
        except ValueError:
            print("Error: Entrada no válida")

    elif opcion == "2":  # Mostrar productos
        print("Mostrando inventario")
        if not inventario:
            print("No hay productos en el inventario.")
        else:
            for p in inventario:
                print(f"Producto: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
                input("\nPresiona Enter para regresar al menú...")

    elif opcion == "3":
        nombre = input("Ingresa el nombre del producto a buscar: ")
        encontrado = False
        for p in inventario:
            if p.nombre == nombre:
                print(f"Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
                encontrado = True
                input("\nPresiona Enter para regresar al menú...")
                break
        if not encontrado:
            print("Producto no encontrado.")


    elif opcion == "4":  # Actualizar producto
        try:
            nombre = input("Ingrese el nombre del producto a actualizar: ").strip().lower()
            nuevo_precio = input("Ingrese el nuevo precio del producto: ").strip()

            if not nuevo_precio:
                raise ValueError("El nuevo precio no puede estar vacío.")

            nombre_encontrado = False

            for p in inventario:
                if p.nombre.strip().lower() == nombre:
                    p.precio = float(nuevo_precio)
                    nombre_encontrado = True
                    print("Precio del producto actualizado.")
                    break

            if not nombre_encontrado:
                print("No se encontró el producto.")

            input("\nPresiona Enter para regresar al menú...")

        except Exception as e:
            print(f"Ha ocurrido un error: {e}")


    elif opcion == "5":
        nombre = input("Ingresa el nombre del producto a eliminar: ").strip()
        for p in inventario:
            if p.nombre == nombre:
                inventario.remove(p)
                print("Producto eliminado.")
                input("\nPresiona Enter para regresar al menú...")
                break
        else:
            print("Producto no encontrado.")

