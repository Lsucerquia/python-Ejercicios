Num1 = 20
Num2 = 6

try:
    print("La división de {0} y {1} es: {2}".format(Num1, Num2, Num1 / Num2))
    Resultado = Num1 / Num2

except ZeroDivisionError:
    print("Error en la ejecución del programa")
    print("Hasta aquí va el programa")