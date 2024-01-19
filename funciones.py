def calculadora(numero1, numero2):
    suma = numero1+numero2
    resta = numero1-numero2

    return suma, resta


numero1 = int(input("introduce el primer numero"))
numero2 = int(input("introduce el segundo numero"))

suma, resta = calculadora(numero1, numero2)
print("suma: ", suma)
print("resta: ", resta)
