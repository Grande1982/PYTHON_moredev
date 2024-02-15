
#forma de mostrar una variable

nombre_usuario = "Cesar"
edad_usuario = 42
salario = 2500.50

print("mi nombre es {} y tengo {} años y gano {}".format(nombre_usuario,edad_usuario,salario))
#otra forma(la mejor de todas)
print("mi nombre es %s y tengo %d años y gano %f" %(nombre_usuario,edad_usuario,salario))
#otra forma menos buena
print("mi nombre es "+ nombre_usuario + " y tengo "+str(edad_usuario)+ " años y gano "+str(salario))
#forma rapida
print(f"mi nombre es {nombre_usuario} y tengo {edad_usuario} años y gano {salario}")


#de string a caracteres
nombre_usuario = "Cesar"
a, b, c, d, e = nombre_usuario
print(a)
print(b)
print(e)

#mostrar carateres desde una posicion inicial(pos2) hasta la final marcada menos 1(pos4). Empezamos en pos 0
nombre_usuario = "Cesar"
parte_nombre_usuario = nombre_usuario[2:5]
print(parte_nombre_usuario)
#tambien se puede hacer cuenta negativo
parte_nombre_usuario = nombre_usuario[-2]
print(parte_nombre_usuario)
#reverse
parte_nombre_usuario = nombre_usuario[::-1]
print(parte_nombre_usuario)

nombre_usuario = "cesar"
#Funciones del sistma con String
#len --> longitud
print(len(nombre_usuario))
#capitalize --> 1ª letra en mayuscula
print(nombre_usuario.capitalize())
#upper --> todo en mayuscula
print(nombre_usuario.upper())
#lower --> todo en minuscular
print(nombre_usuario.lower())
#count --> cuenta el numero de "e"
print(nombre_usuario.count("e"))
#isnumeric --> es numero
print(nombre_usuario.isnumeric())
#isnumeric --> es letras
print(nombre_usuario.isalpha())
#startswith --> comienza(diferecnia mayusculas de minusculas)
print(nombre_usuario.startswith("c"))


