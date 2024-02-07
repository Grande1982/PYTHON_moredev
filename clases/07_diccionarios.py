mi_diccionario = dict()

#otra forma de definir un diccionario
mi_diccionario2 = {}
print(type(mi_diccionario2))

mi_diccionario2 ={"Nombre":"Cesar", "Apellido":"Grande", "Edad":41}
print(mi_diccionario2)

mi_diccionario3 = {
    "Nombre":"Juan", 
    "Apellido":"Cobo", 
    "Lenguajes":{"Español","Ingles", "Aleman"}
    }

#diccionario con una clave:valor que el valor es un set
print(mi_diccionario3)

#acceder al valor
print(mi_diccionario3["Nombre"])
#cambiamos el valor
mi_diccionario3["Nombre"] = "Ruth"
print(mi_diccionario3)

#añadir datos al diccionario
mi_diccionario3["Sueldo"] = 26000
print(mi_diccionario3)

#borrar elemento
del mi_diccionario3["Apellido"]
print(mi_diccionario3)

#comprobar si tenemos algun dato en el diccionario pero busca por clave
print("Nombre" in mi_diccionario3)
print("Juan" in mi_diccionario3)

#operaciones
print(mi_diccionario3.keys())
mi_diccionario4 = mi_diccionario3.copy()
print("diccionadio es:",mi_diccionario4)

#copiar el diccionario unicamente las claves
mi_diccionario5 = dict.fromkeys(mi_diccionario2)
print(mi_diccionario5)

