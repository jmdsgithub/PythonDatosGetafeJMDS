import oracledb
from models.empleado import Empleado

class ServiceOracleEmpleados:
    def __init__(self):
        self.connection=self.connection=oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

    def getEmpleados(self):
        sql='select * from EMP'
        cursor=self.connection.cursor()
        cursor.execute (sql)
        data:list[Empleado]=[]
        for row in cursor:
            emp=Empleado()
            emp.idempleado=row[0]
            emp.apellido=row[1]
            emp.oficio=row[2]
            emp.salario=row[5]
            data.append(emp)
        cursor.close()
        return data

    def getEmpleadosSalario(self,salario):
        sql='select * from EMP where SALARIO >= :p1'
        cursor=self.connection.cursor()
        cursor.execute(sql,  (salario, ))
        data:list[Empleado]=[]
        for row in cursor:
            emp=Empleado()
            emp.idempleado=row[0]
            emp.apellido=row[1]
            emp.oficio=row[2]
            emp.salario=row[5]
            data.append(emp)
        cursor.close()
        return data