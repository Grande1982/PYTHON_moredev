
class Person:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

mi_persona = Person("Cesar","Grande")
print(mi_persona.nombre, mi_persona.apellido)

print(f"{mi_persona.nombre} {mi_persona.apellido}")