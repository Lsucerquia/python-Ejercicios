
diccionario= {"azul":"blue","a":"A",}
diccionario["uno"]=1
print(diccionario["azul"])
diccionario["azul"]="BLUE"
print(diccionario)

del (diccionario["a"])
print(diccionario)

diccionario={"pedro":{"edad":22,"estatura":1.65},"ana":{"edad":25,"estatura":1.70},"maria":[30,1.75]}
print(diccionario["pedro"])

#ciclo for
nums =[4,78,9,81]
for n in nums:
    print(n)

print("")
for i in range(0,5):
    print(i)

    if i==2:
        print("o.k")

print("")

for i in range (10,-1,-1):
    print(i)
    if i==2:
        print("o.k")



#bucle infinito
"""
x=1
while x < 10:
    print(x)
"""

