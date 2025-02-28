import platform
if platform.system() == "Windows":
    instant_client_dir = r"C:\Oracle\instantclient_23_7"
import oracledb
oracledb.init_oracle_client(lib_dir=instant_client_dir)
from models import departamento

class ServiceOracleDepartamentos:
    def __init__(self):
        self.connection=oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

    def eliminarDepartamento(self, numero):
        sql='delete from DEPT where DEPT_NO=:p1'
        cursor=self.connection.cursor()
        cursor.execute(sql, (numero,))
        registros=cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros

    def buscarDepartamentoId(self, numero):
        sql='select * from DEPT where DEPT_NO=:p1'
        cursor=self.connection.cursor()
        cursor.execute(sql, (numero,))
        row=cursor.fetchone()
        modelo = departamento.Departamento()
        modelo.numero=row[0]
        modelo.nombre=row[1]
        modelo.localidad=row[2]
        cursor.close()
        return modelo
    
    def modificarDepartamento(self, nombre, localidad, numero, viejonumero):
        sql='update DEPT set DNOMBRE=:p1, LOC=:p2, DEPT_NO=:p3 where DEPT_NO=:p4'
        cursor=self.connection.cursor()
        cursor.execute(sql, (nombre, localidad, numero, viejonumero))
        registros=cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros

    def insertarDepartamento(self, numero, nombre, localidad):
        sql='insert into DEPT values (:id, :nombre, :localidad)'
        cursor=self.connection.cursor()
        cursor.execute(sql, (numero, nombre, localidad))
        registros=cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
    
    def getAllDepartamentos(self):
        sql='select * from DEPT'
        cursor=self.connection.cursor()
        cursor.execute(sql)
        datos=[]
        for row in cursor:
            dept=departamento.Departamento()
            dept.numero=row[0]
            dept.nombre=row[1]
            dept.localidad=row[2]
            datos.append(dept)
        cursor.close()
        return datos
