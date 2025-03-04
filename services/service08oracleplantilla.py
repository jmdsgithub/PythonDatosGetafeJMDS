import oracledb
from models.plantilla import Plantilla

class ServiceOraclePlantilla:
    def __init__(self):
        self.connection=self.connection=oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

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
        sql='update PLANTILLA set SALARIO=SALARIO+:p1 where HOSPITAL_COD=:p2'
        cursor=self.connection.cursor()
        cursor.execute(sql, (incremento, hospital))
        registros:list[Plantilla]=cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
