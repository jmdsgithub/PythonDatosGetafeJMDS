from services import service05oracledoctores as service
from models import doctor as model

print('-------CRUD DOCTORES--------')

servicio=service.ServiceOracleDoctores()
doctores=servicio.getAllDoctores()
for doc in doctores:
    print(f'{doc.apellido}, Especialidad: {doc.especialidad}, {doc.salario}')

print('Seleccione una opción: ')
print('1.- Insertar doctor ')
print('2.- Eliminar Doctor: ')
print('3.- Modificar doctor ')

opcion=int(input())
if (opcion ==1):
    print('Id del doctor: ')
    idDoctor=int(input())
    print('Apellido: ')
    ape=input()
    print('Especialidad: ')
    espe=input()
    print('Salario: ')
    sal=int(input())
    print('Hospital')
    hospital=int(input())
    reg=servicio.insertarDoctor(idDoctor, ape, espe, sal, hospital)
    print(f'Doctores insertados: {reg}')
elif (opcion==2):
    print('Id del Doctor a eliminar: ')
    idDoctor=int(input())
    registros=servicio.eliminarDoctor(idDoctor)
    print(f'Registros eliminados: {registros}')
elif (opcion==3):
    print('Id del doctor a modificar: ')
    idDoctor=int(input())
    print('Nuevo apellido: ')
    ape=input()
    print('Nueva especialidad: ')
    espe=input()
    print('Nuevo salario: ')
    sal=int(input())
    print('Hospital')
    hosp=int(input())
    registros=servicio.modificarDoctor(idDoctor, ape, espe, sal, hosp)
    print(f'Doctores modificados: {registros}')

print('Fin de programa')
