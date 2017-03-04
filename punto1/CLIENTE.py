# INICIO DEL PROGRAMA

import socket

cliente = socket.socket()

"""direccion ip del servidor, puerto del servidor, nos conectamos con el metodo connect"""

cliente.connect(("localhost", 35000))

while True:

    mensaje_cliente = raw_input("USUARIO >>: ")
    cliente.send(mensaje_cliente)

    clave = raw_input(("CONTRASENA >>: "))
    cliente.send(clave)
    print 'BIENVENIDO'

    if (mensaje_cliente == 'fausto' and clave == 'luciana'):
        print "********* CALCULAD0RA **********"

    else:
        print'No puede Acceder'
        break

    lista = ['1. suma', '2. Resta', '3. Multiplicacion', '4. Division', '5. salir']

    for i in lista:
            print i

    import operaciones

    operaciones.suma()
    operaciones.resta()
    operaciones.producto()
    operaciones.division()

    if mensaje_cliente == "salir":

        break

print "hasta la proxima"
cliente.close()
















