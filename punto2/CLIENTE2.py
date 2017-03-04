# INICIO DEL PROGRAMA

import socket

cliente = socket.socket()

"""direccion ip del servidor, puerto del servidor"""

cliente.connect(("localhost", 35000))

while True:

    import opciones

    opciones.crear()
    opciones.modificar()
    opciones.eliminar()

    if mensaje_cliente == "salir":

        break
print "vuelva cuando quiera"
cliente.close()

