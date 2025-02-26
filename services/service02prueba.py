from models import mascota

#Este servicio será el que tendra métodos para ser utilizados en el main

def getSaludo():
    return 'Bienvenido a Sql Server'

def getMascota1():
    dato1=mascota.Mascota()
    dato1.nombre='Patricio'
    dato1.raza='PEstrella de mar'
    dato1.edad=8
    return dato1

def getMascota2():
    dato2=mascota.Mascota()
    dato2.nombre='Sebastián'
    dato2.raza='Cangrejo'
    dato2.edad=8
    return dato2