print("++++++++++++++++++")
print("+++menu++")
print("++++++++++++++++++")

menu = """
Bienvenido al registro de usuarios, por favor digite la opción que desea
a continuación seleccione del 1 al 3:

[1] Digite su nombre
[2] Digite su edad
[3] Digite su correo electrónico
"""
print(menu)

opcion = input("Digite una opción del 1 al 3: ")

if opcion == '1':
    nombre = input('Digite su nombre: ')
    if nombre.isalpha():  # Verifica que el nombre solo contenga letras
        print("Su nombre es:", nombre)
        print("Su nombre es: {}".format(nombre))
    else:
        print("Has digitado un nombre no válido")

elif opcion == '2':
    edad = input('Digite su edad: ')
    if edad.isdigit():  # Verifica que la edad solo contenga dígitos
        print("Tu edad es: " + edad)
        print("Tu edad es:", edad)
        print("Tu edad es: {}".format(edad))
    else:
        print("Has digitado una edad no válida")

elif opcion == '3':
    email = input('Digite su correo electrónico: ')

    if email.find("@") >= 0 and email.find(".") >= 0:
        # Verifica que el correo contenga '@' y '.'
        print("Tu correo es:", email)
        print("Tu correo es:", email)
        print("Tu correo es: {}".format(email))
    else:
        print("El email está mal escrito")

else:
    print("Debes digitar un número entre 1 y 3")
    print("******" * 20)