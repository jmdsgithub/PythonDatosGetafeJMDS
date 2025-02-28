from services import service06oraclehospitales as service
from models import hospital as model

print('-------CRUD DOCTORES--------')

servicio=service.ServiceOracleHospitales()
hospitales=servicio.getAllHospitales()
for hosp in hospitales:
    print(f'HOSPITAL_COD: {hosp.codigo}, NOMBRE: {hosp.nombre}, DIRECCION: {hosp.direccion}, TELEFONO: {hosp.telefono}, NUM_CAMA: {hosp.camas}')

print('Seleccione una opción: ')
print('1.- Insertar Hospital ')
print('2.- Eliminar Hospital ')
print('3.- Modificar Hospital ')

opcion=int(input())
if (opcion ==1):
    print('Código del Hospital: ')
    codigo=int(input())
    print('Nombre del Hospital: ')
    hospital=input()
    print('Dirección del hospital: ')
    direccion=input()
    print('Teléfono del Hospital: ')
    telefono=int(input())
    print('Número de camas del Hospital: ')
    camas=int(input())
    reg=servicio.insertarHospital(codigo, hospital, direccion, telefono, camas)
    print(f'Hospitales insertados: {reg}')