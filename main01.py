from services import service01prueba as service
from models import persona

saludo=service.getSaludo()
print('Todo OK, ' + saludo)

pez=service.getMascota1()
leona=service.getMascota2()
print(pez.nombre)
print(leona.nombre)