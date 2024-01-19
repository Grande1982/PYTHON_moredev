selector = 10
while selector !=0:
    print("MENU")
    print("********")
    print("1-Suma")
    print("2-Resta")
    print("3-Multiplicacion")
    print("4-Division")
    print("0-Salir")

    selector = int(input("Seleccione la operacion que desee realizar: "))
    numero1 = int(input("Introduce el primer numero: "))
    numero2 = int(input("Introduce el segundo numero: "))

    if selector == 1:
        print("El resultado es: ",numero1+numero2)
        
    elif selector == 2:
        print("El resultado es: ",numero1-numero2)

    elif selector == 3:
        print("El resultado es: ",numero1*numero2)

    elif selector == 4:
        print("El resultado es: ",numero1/numero2)

    else:
        selector = 0
        print("Adios")


    
    
                      
