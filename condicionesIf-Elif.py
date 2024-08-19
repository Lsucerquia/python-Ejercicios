#actividad menu
print("++++++++++++++++++")
print("++++conversor+++++")
print("++++++++++++++++++")

print("\nMenu de opciones: \n")
menu= '''
print("presiona 1 para convertir de numero a palabra")
print("presiona 2 para convertir de palabra a numero")
'''
print (menu)
option= int(input("Cual es la opcion deseadad:?"))
if option ==1:
    print("\n conversor de numero a palabra.\n")
    option_uno =int(input("Cual es el numero que desea convertir?"))
    if option_uno==1:
        print("El numero es uno")
    elif option_uno==2:
        print("El numero es dos")
    elif option_uno == 3:
        print("El numero es tres")
    elif option_uno == 4:
        print("El numero es cuatro")
    elif option_uno == 5:
        print("El numero es cinco")
    else:
        print("El numero digitado no esta registrado")

elif option ==2:
    print("\n Conversor de palabra a numero\n")
    #option_dos=input("Cual es la palabra del numero que desea convertir ")
    #option_dos = option_dos.lower()
    option_dos =(input("Cual es la palabra del numero que desea convertir ")).lower()
    if option_dos=="uno":
        print("El numero es 1")
    elif option_dos=="dos":
        print("El numero es 2")
    elif option_dos == "tres":
        print("El numero es 3")
    elif option_dos == "cuatro":
        print("El numero es 4")
    elif option_dos == "cinco":
        print("El numero es 5")
    else:
        print("la palabra no esta registrado")
else:
    print("opcion no valida")

