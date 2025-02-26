from services import service02prueba as service
from models import persona

saludo=service.getSaludo()
print('Todo OK, ' + saludo)

dato1=service.getMascota1()
dato2=service.getMascota2()
print(dato1.nombre, dato1.raza, dato1.edad)
print(dato2.nombre, dato2.raza, dato2.edad)

dato1=service.getMascota1()
print(dato1)
dato2=service.getMascota2()
print(dato2)