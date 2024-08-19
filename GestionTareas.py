class GestionTareas:

    def __init__(self, titulo, descripcion, estado):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    @staticmethod
    def Mostrar_menu():
        print("\nGestión de tareas")
        print("1. Agregar Nuevas tareas")
        print("2. Mostrar todas las tareas")
        print("3. Buscar una tarea por título")
        print("4. Actualizar el estado de una tarea")
        print("5. Eliminar una tarea por título")
        print("6. Salir del programa")


Tareas = []

while True:
    GestionTareas.Mostrar_menu()
    try:
        opcion = input("Elige una opción: ").strip()

        if opcion == "6":
            print("Saliendo del programa")
            break

        if opcion == "1":
            try:
                titulo = input("Ingrese el título de la tarea: ").strip()
                descripcion = input("Ingrese una descripción para esa tarea: ").strip()
                estado = input("Ingrese un estado para esa tarea: ").strip()

                if not titulo or not descripcion or not estado:
                    raise ValueError("El título, la descripción y el estado no pueden estar vacíos.")

                tarea = GestionTareas(titulo, descripcion, estado)
                Tareas.append(tarea)
                print(f"Tarea agregada: {tarea.titulo}, {tarea.descripcion}, {tarea.estado}")
                input("\nPresiona Enter para regresar al menú...")

            except ValueError as e:
                print(f"Error al agregar la tarea: {e}")

        elif opcion == "2":
            try:
                if Tareas:
                    print("\nLista de tareas:")
                    for t in Tareas:
                        print(f"Título: {t.titulo}, Descripción: {t.descripcion}, Estado: {t.estado}")
                else:
                    print("No hay tareas registradas.")

                input("\nPresiona Enter para regresar al menú...")

            except Exception as e:
                print(f"Error al mostrar las tareas: {e}")

        elif opcion == "3":
            try:
                titulo = input("Ingrese el título de la tarea a buscar: ").strip().lower()
                encontrado = False

                for t in Tareas:
                    if t.titulo.strip().lower() == titulo:
                        print(f"Título: {t.titulo}, Descripción: {t.descripcion}, Estado: {t.estado}")
                        encontrado = True
                        break

                if not encontrado:
                    print("No se encontró una tarea con el título dado.")

                input("\nPresiona Enter para regresar al menú...")

            except Exception as e:
                print(f"Error al buscar la tarea: {e}")

        elif opcion == "4":
            try:
                titulo = input("Ingrese el título de la tarea a actualizar: ").strip().lower()
                nuevo_estado = input("Ingrese el nuevo estado de la tarea: ").strip()

                if not nuevo_estado:
                    raise ValueError("El nuevo estado no puede estar vacío.")

                tarea_encontrada = False

                for t in Tareas:
                    if t.titulo.strip().lower() == titulo:
                        t.estado = nuevo_estado
                        tarea_encontrada = True
                        print("Estado de la tarea actualizado.",nuevo_estado)
                        break

                if not tarea_encontrada:
                    print("No se encontró una tarea con el título dado.")

                input("\nPresiona Enter para regresar al menú...")

            except Exception as e:
                print(f"Error al actualizar la tarea: {e}")

        elif opcion == "5":
            try:
                titulo = input("Ingrese el título de la tarea a eliminar: ").strip().lower()
                tarea_a_eliminar = None

                for t in Tareas:
                    if t.titulo.strip().lower() == titulo:
                        tarea_a_eliminar = t
                        break

                if tarea_a_eliminar:
                    Tareas.remove(tarea_a_eliminar)
                    print("Tarea eliminada.")
                else:
                    print("No se encontró una tarea con el título dado.")

                input("\nPresiona Enter para regresar al menú...")

            except Exception as e:
                print(f"Error al eliminar la tarea: {e}")

        else:
            print("La opción no es válida. Por favor, elige una opción del menú.")
            input("\nPresiona Enter para regresar al menú...")

    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")