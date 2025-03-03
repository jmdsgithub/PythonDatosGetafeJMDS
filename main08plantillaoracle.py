from services import service08oracleplantilla as service
from models.plantilla import Plantilla

print('Probando conexión a Base de Datos')
print('------PLANTILLA-------')

servicio=service.ServiceOraclePlantilla()
plantilla=servicio.getPlantilla()
for emp in plantilla:
    print(f'idPlantilla: {emp.idPlantilla}, Apellido: {emp.apellido}, Función: {emp.funcion}, Salario: {emp.salario}, Hospital {emp.hospital}')

print('------AUMENTO DE SALARIOS DE PLANTILLA POR HOSPITAL-------')

print('Introduzca el HOSPITAL_COD del hospital a modificar: ')
hospital=input()
print('Introduzca el nuevo salario: ')
salario=int(input())
registros=servicio.updateSalarioPlantilla(salario, hospital)
print(f'Registros modificados: {registros}')

print('Fin de programa')
