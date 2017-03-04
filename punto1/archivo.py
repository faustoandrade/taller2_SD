import datetime

def archivos():
    archivo = open("Registro.txt", 'a')
    archivo.close()
archivos()

def escribir():
    archivo = open("Registro.txt", "a", )

    nombre = raw_input('ingrese Nombre: ')
    archivo.write('\nnombre: ')
    archivo.write(nombre)


    contrasena = raw_input('ingrese contrasena: ')
    archivo.write('\ncontrasena: ')
    archivo.write(contrasena)

    fecha = str(datetime.datetime.now())
    archivo.write('\n:Fecha y Hora ')
    archivo.write(fecha)
escribir()
