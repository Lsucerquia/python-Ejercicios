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
    print("Su nombre es: " + nombre)
    print("Su nombre es:", nombre)
    print("Su nombre es: {}".format(nombre))

elif opcion == '2':
    edad = input('Digite su edad: ')
    print("Su edad es: " + edad)
    print("Su edad es:", edad)
    print("Su edad es: {}".format(edad))

elif opcion == '3':
    email = input('Digite su correo electrónico: ')
    print("Su correo electrónico es: " + email)
    print("Su correo electrónico es:", email)
    print("Su correo electrónico es: {}".format(email))

else:
    print("Debes digitar un número entre 1 y 3")
    print("******" * 20)

# Código adicional
año = 2022
evento = 'Semana Santa'
print(f'Lo mejor de las fiestas de {evento} del {año}')

flor = 'Rosas'
print(f'El jardín de mi casa está lleno de {flor}')

modelo = 'opción Tucán'
precio = 1900000
impuesto = precio * 19 / 100
print(f'La bicicleta {modelo} tiene un valor de: ${precio + impuesto} pesos')


