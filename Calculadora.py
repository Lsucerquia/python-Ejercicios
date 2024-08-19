
def Suma(a , b):
    return a + b

def Resta(a , b):
    return a-b

def Multiplicacion(a, b):
    return a * b

def Division(a, b):
    if b !=0:
        return a/b
    else:
        return 'error'

def Mostrar_Menu():
    print('calculadora Basica')
    print('1:Suma')
    print('2:Resta')
    print('3:Multiplicaion')
    print('4:Division')
    print('5:Salir')

while True:
    Mostrar_Menu()
    opcion=input("elegir una opcion ")
    if opcion ==" 5 ":
        print("salir del programa ")
        break

    if opcion in ["1","2","3","4"]:
        num1=int(input("ingrese el primer numero "))
        num2= int(input("ingrese el segundo numero "))

        if opcion == "1":
            print(f"resultado es:{Suma(num1,num2)}")
        elif opcion == "2":
            print(f"resultado es:{Resta(num1, num2)}")
        elif opcion == "3":
            print(f"resultado es:{Multiplicacion(num1, num2)}")
        elif opcion == "4":
            print(f"resultado es:{Division(num1, num2)}")
        else:
            print("Opcion no valida, por favor intentar de nuevo")






S