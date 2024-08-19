# if condicion_logica:

if (True):
    print("Se ha ingresado a la estructura de control condicional if")


#sentencias condicionales simples
num_1 = 5
if num_1 == 5:
    print("el numero es 5")
    print("Fin")

#divicion entera con condicional
a = 4
b = 2
if b != 0:
    print(a/b)


#ejercicio sacar promedio de notas, sentencias condicionale compuestas
print("sistema para calcular el promedio de notas de un  estudiante")
name = input("Por favor digitar nombre")
nota_1 = float(input(name + "digitalizar nota 1:"))
nota_2 = float(input(name + "digitalizar nota 2:"))
nota_3 = float(input(name + "digitalizar nota 3:"))
prom = (nota_1 + nota_2 + nota_3)/3
prom = float(prom)

if prom >= 3:
    print("Felicitaciones" + name, "Aprobaste y tu promedio es:", prom)
    print("Felicitaciones" + name, "Aprobaste y tu promedio es:", round(prom,3))
else:
    print("Lo siento" + name, "Reprobaste y tu promedio es:", prom)
    print("Lo siento" + name, "Reprobaste y tu promedio es:",round(prom, 3))
    print("Fin")


#sentencias condicionales smultiples
"""
if condicion_logica:
    instruccion
elif condicion_logica:
    instruccion
else:
"""

x=5
if x==5:
    print("es 5")
else:
     print("no lo es")

#ejercicio
x=5
if x==5:
    print("es 5")
elif x==6:
     print("es 6")
elif x ==7:
    print("es 7")

# actividad 1
print("*******************")
print("convertir")
print("*******************")

num_1 = int(input("Cual es el numero que desea convertir"))
if num_1 == 1:
    print("El numero es Uno ")
elif num_1 == 2:
    print("El numero es dos")
elif num_1 == 3:
    print("El numero es tres")
elif num_1 == 4:
    print("El numero es cuatro")
elif num_1 == 5:
    print("El numero es cinco")
else:
    print("El numero digitado no esta en lista")
print("Fin")

#convertir una cadena a minusculas
cadena ="Hola Jose"
print(cadena.lower())

#convertir una cadena a mayusculas
cadena ="Hola Jose"
print(cadena.upper())

#convertir una cadena a mayusculas a nimusculas y viceversa
cadena ="Hola Jose"
print(cadena.swapcase())

#convertir una cadena en formato titulo
cadena ="hola Jose"
print(cadena.title())
