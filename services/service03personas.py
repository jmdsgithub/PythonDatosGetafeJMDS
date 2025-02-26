from models import persona

#'''Este servicio será el que tendra métodos para ser utilizados en el main'''

def getSaludo():
    return 'Bienvenido a Persona'

def getPersona1():
    dato1=persona.Persona()
    dato1.nombre='PP11'
    dato1edad=22
    dato1.email='pp11@gmail.com'
    return dato1

def getPersona2():
    dato2=persona.Persona()
    dato2.nombre='PP22'
    dato2.edad=44
    dato2.email='pp22@gmail.com'
    return dato2