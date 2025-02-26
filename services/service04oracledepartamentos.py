import oracledb
from models import departamento

class ServiceOracleDepartamentos:
    def __init__(self):
        self.connection=oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

    def buscarDepartamento(self, numero):
        sql='select * from DEPT where DEPT_NO=:p1'
        cursor=self.connection,cursor()
        cursor.execute(sql, (numero,))
        row=cursor.fetchone()
        modelo = departamento.Departamento()
        modelo.numero=row[0]
        modelo.numero=row[1]
        modelo.numero=row[2]
        cursor.close()
        return modelo

    def insertarDepartamento(self, numero, nombre, localidad):
        sql='insert into DEPT values (:id, :nombre, :localidad)'
        cursor=self.connection.cursor()
        cursor.execute(sql, (numero, nombre, localidad))
        registros=cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
    

