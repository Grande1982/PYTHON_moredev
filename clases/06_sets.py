mi_set = set()
print(type(mi_set))
#otra forma de definir un set
mi_set2 = {}
print(type(mi_set2))

mi_set2 = {"cesar",1,3,"grande"}
print(type(mi_set2))

#añadir
mi_set2.add("ruth")
print(mi_set2)
#buscar en el sets
print("cesar" in mi_set2)
#eliminar valor
mi_set2.remove(3)
print(mi_set2)

mi_set2.clear()
print(mi_set2)
del mi_set2

mi_set3 = {"xx",10,30,"zz","grande"}

#unir sets
mi_set2 = mi_set3.union(mi_set2)
print(mi_set2)

#diferencia (los valores que este en mi_set3 dentro del 2 no seran imprimidos)
print(mi_set2.difference(mi_set3))

