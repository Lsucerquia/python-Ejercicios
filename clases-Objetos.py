

class Auto:
    Marca='Mazda'
    Modelo='2014'

taxi= Auto()
print(taxi.Marca)
print(taxi.Modelo)


class Humano:#atributos
    def __init__(self,edad,nombre,ocupacion):
        self.edad=edad
        self.nombre=nombre
        self.ocupacion=ocupacion

#crear objetos que tiene todos los atributos del humano
persona_1=Humano(34,'maria','ingeniero')
print(persona_1.edad)
print(persona_1.nombre)
print(persona_1.ocupacion)
print('soy', persona_1.nombre,'mi edad es:',persona_1.edad,'mi ocupacion es:',persona_1.ocupacion)


