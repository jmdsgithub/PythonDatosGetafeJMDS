from models import mascota

#Este servicio será el que tendra métodos para ser utilizados en el main

def getSaludo():
    return 'Bienvenido a Sql Server'

def getMascota1():
    dato=mascota.Mascota()
    dato.nombre='Patricio'
    dato.raza='PEstrella de mar'
    dato.edad=8
    return dato

def getMascota2():
    dato=mascota.Mascota()
    dato.nombre='Sebastián'
    dato.raza='Cangrejo'
    dato.edad=8
    return dato