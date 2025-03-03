from services import service07mysqlempleados as service
from models.empleado import Empleado

print('Probando conexión a Base de Datos')
servicio=service.ServiceMySqlEmpleados()
empleados=servicio.getEmpleados()
for emp in empleados:
    print(f'Apellido: {emp.apellido}, Oficio {emp.oficio}, Salario {emp.salario}')

print('Introduzca un salario a consultar: ')
salario=int(input())
empleados=servicio.getEmpleadosSalario(salario)
for emp in empleados:
    print(f'Apellido: {emp.apellido}, Oficio {emp.oficio}, Salario {emp.salario}')
    print('Fin de programa')