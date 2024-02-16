
class Person:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

mi_persona = Person("Cesar","Grande")
print(mi_persona.nombre, mi_persona.apellido)

print(f"{mi_persona.nombre} {mi_persona.apellido}")

#Encapsulacion
class PersonPrivado:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def get_name(self):
        return self.__nombre
    
    def set_name(self,nombre):
        self.__nombre = nombre


mi_persona2 = PersonPrivado("Ruth","Vega")
print(mi_persona2.get_name())
mi_persona2.set_name("Jose")
print(mi_persona2.get_name())

     