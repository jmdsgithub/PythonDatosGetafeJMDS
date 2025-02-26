from services import service03personas as service
from models import mascota

saludo=service.getSaludo()
print('Todo OK, ' + saludo)

dato1=service.getPersona1()
dato2=service.getPersona2()
print(f'Nombre: {dato1.nombre}, email: {dato1.email}, Edad: {dato1.edad}')
print(dato2.nombre, dato2.email, dato2.edad)

print('Fin de programa')