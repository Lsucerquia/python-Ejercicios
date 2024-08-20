class Contacto:
    # Definimos la clase y el nombre de la clase
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

def mostrar_menu():
    print("\nGestión de contactos")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

contactos = []

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ").strip()

    if opcion == "5":
        print("Saliendo del programa.")
        break

    if opcion == "1":
        nombre = input("Ingrese un nombre: ").strip()
        telefono = input("Ingrese el teléfono: ").strip()
        contacto = Contacto(nombre, telefono)  # Crear una instancia de Contacto

        # Agregar a la lista de contactos
        contactos.append(contacto)  # Agregar el objeto contacto a la lista
        print("Contacto agregado.")

    elif opcion == "2":  # Para mostrar contactos
        print("Mostrando contactos")
        if not contactos:
            print("no hay contactos para mostrar")
        else:
            for c in contactos:
                print(f"Contactos:{c.nombre},telefono:{c.telefono}")
                input("\n Presiona Enter para regresar al menu")


    elif opcion == "3":
        nombre = input("Ingresa el nombre a buscar: ").strip()
        encontrado = False
        for c in contactos:
            if c.nombre == nombre:
                print(f"Nombre: {c.nombre}, Teléfono: {c.telefono}")
                encontrado = True
                break

        if not encontrado:
            print("Contacto no encontrado.")



    elif opcion == "4":
        nombre = input("Ingresa el nombre del contacto a eliminar: ").strip()
        for c in contactos:
            if c.nombre == nombre:
                contactos.remove(c)  # Se debe usar la lista 'contactos' para eliminar
                print("Contacto eliminado.")
                break
        else:
            print("Contacto no encontrado.")


