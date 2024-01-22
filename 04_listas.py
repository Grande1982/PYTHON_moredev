"""

mi_lista = list()
#otra forma de definir una lista
mi_lista2 = []

#forma de calcular longitud de la lista
mi_lista = [42,"grande",1,"cesar"]
print(len(mi_lista))

print(type(mi_lista))
print(type(mi_lista2))

#accedemos a la lista(primer elemento es 0)
print(mi_lista[2])
#podemos acceder contando desde el final
print(mi_lista[-3])


mi_lista = [42,"grande",1,"cesar"]
edad, apellidos, num_hijos, nombre = mi_lista
print(nombre)

nombre, apellidos, num_hijos, edad,  = mi_lista[3],mi_lista[1],mi_lista[2],mi_lista[0]
print(nombre)
"""
mi_lista = [42,"grande",1,"cesar"]
mi_lista2 = ["juan","grande",5,"ruth"]
"""
print(mi_lista)
print(mi_lista2)
#print(mi_lista+mi_lista2)

#añadir elementos a la lista al final
mi_lista.append("conde")
#añadir elementos en el indice y objeto a insertar
mi_lista.insert(2,"azul")
#print(mi_lista)
#print(mi_lista2)
#elimnar
mi_lista2.remove("grande")
print(mi_lista2)
#elimnar otra forma usando pop (por defecto ultimo valor) 
mi_lista2.pop()
print(mi_lista2)
#elimnar otra forma usando pop y pasando indice
mi_lista2.pop(1)
print(mi_lista2)
#eliminar elemento por indice
del mi_lista2[0]
print(mi_lista2)
#eliminar lista
print(mi_lista)
mi_lista.clear()
print(mi_lista)
"""
"""
#copiar lista
mi_lista_copiada = []
print(mi_lista_copiada)
mi_lista_copiada = mi_lista.copy()
print(mi_lista)
print(mi_lista_copiada)
#reverse de lista
mi_lista_copiada.reverse()
print(mi_lista_copiada)

#ordena la lista
lista_numero = [1,100,2,500,9,8,10,100]
print(lista_numero)
lista_numero.sort()
print(lista_numero)
"""
#mostrar del indice 2 al 6
lista_numero = [1,100,2,500,9,8,10,100]
print(lista_numero)
print(lista_numero [3:7])











