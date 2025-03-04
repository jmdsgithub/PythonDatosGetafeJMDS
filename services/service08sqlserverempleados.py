import pyodbc
from models.plantilla import Plantilla

class ServiceSqlServerEmpleados:
    def __init__(self):
        self.connection=pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=127.0.0.1;DATABASE=HOSPITAL;UID=SA;PWD=Getafe12345@@;TrustServerCertificate=yes')

    def getPlantilla(self):
        sql='select * from PLANTILLA'
        cursor=self.connection.cursor()
        cursor.execute (sql)
        data:list[Plantilla]=[]
        for row in cursor:
            emp=Plantilla()
            emp.idPlantilla=row[2]
            emp.apellido=row[3]
            emp.funcion=row[4]
            emp.salario=row[6]
            emp.hospital=row[0]
            data.append(emp)
        cursor.close()
        return data

    def updateSalarioPlantilla(self,salario, hospital):
        sql='update PLANTILLA set SALARIO=SALARIO+? where HOSPITAL_COD=?'
        cursor=self.connection.cursor()
        cursor.execute(sql, (incremento, hospital))
        registros:list[Plantilla]=cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros