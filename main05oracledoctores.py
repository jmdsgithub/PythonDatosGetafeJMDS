from services import service05oracledoctores as service
from models import doctor as model

print('-------CRUD DOCTORES--------')

servicio=service.ServiceOracleDoctores()
doctores=servicio.getAllDoctores()
for doc in doctores:
    print(f'{doc.apellido}, Especialidad: {doc.especialidad}, {doc.salario}')

print('Fin de programa')
