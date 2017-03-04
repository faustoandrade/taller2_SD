def suma():
    opc = int(input("Selecione una Opcion: "))
    if (opc == 1):
        x = int(input("Ingrese un Numero: \n"))
        y = int(input("Ingrese el siguiente numero: \n"))

        print "La Suma es: ", x+y
suma()

def resta():
    opc = int(input("Selecione una Opcion: "))
    if (opc == 2):
        x = int(input("Ingrese Numero: \n"))
        y = int(input("Ingrese El siguiente Numero: \n"))

        print "La Resta es: ", x-y
resta()


def producto():
    opc = int(input("Selecione una Opcion: "))
    if (opc == 3):

        x = int(input("Ingrese un Numero: \n"))
        y = int(input("Ingrese el siguinte Numero: \n"))
        print "El producto es: ", x * y
producto()


def division():
    opc = int(input("Selecione una Opcion: "))
    if (opc == 4):
        x = int(input("Ingrese un Numero: \n"))
        y = int(input("Ingrese el siguiente Numero: \n"))

        print "La division es: ", x / y
division()

