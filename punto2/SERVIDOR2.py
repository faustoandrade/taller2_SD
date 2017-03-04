# INICIO DEL PROGRAMA

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("", 35000))
server.listen(1)

socket_cliente, direccion = server.accept()

while True:

    import opciones
    entrada=opciones.menu()
    cliente.send(entrada)
    salir = socket_cliente.recv(1024)
    if salir == "salir":
        print "Hasta Pronto"
        socket_cliente.close()
        server.close()