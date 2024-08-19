

def holaConNombre(nombre):
    print("Hola" + nombre + "!")


def suma (n1,n2):
    print(n1 +n2)
suma(3,4)

"""tabla de multiplicar"""

def mul_por_5 (num):
    print(f'{num}*5={num*5}')
    print('inicio')


def saludo(nombre):
    print('hola {}'.format(nombre))
    print("el resultado es: ")

def gracias(agradecer):
    print('gracias{}'.format(agradecer))
print('por su respuesta')

saludo('ana')
gracias(' carlos')

def suma(a, b=4):
    return a+b
def resta (a,b):
    return a-b
resultSuma=suma(3)
resultResta=resta(a=5,b=3)
print(resultSuma)
print(resultResta)

"""realizar porgrama que capture dos valores, los compare y determine cual es el mayor"""
def numMayor(n1,n2):
    if n1>n2:
        max =n1
    else:
        max= n2
        return  max
print('digitar primer numero')
n1=int(input('por favor digitar el numero 1'))
n2=int(input('por favor digitar el numero 2'))
mayor= numMayor(n1,n2)
print('el resultado mayor es:', mayor)
