import oracledb
from models import hospital as model

class ServiceOracleHospitales:
    def __init__(self):
        self.connection=oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

    def getAllHospitales(self):
        sql='select * from HOSPITAL'
        cursor=self.connection.cursor()
        cursor.execute(sql)
        datos=[]
        for row in cursor:
            hosp=model.Hospital()
            hosp.codigo=row[0]
            hosp.nombre=row[1]
            hosp.direccion=row[2]
            hosp.telefono=row[3]
            hosp.camas=row[4]
            datos.append(hosp)
        cursor.close()
        return datos
    
    def insertarHospital(self, codigo, nombre, direccion, telefono, camas):
        sql='insert into HOSPITAL values ( :codigo, :nombre, :direccion, :telefono, :camas)'
        cursor=self.connection.cursor()
        cursor.execute(sql, (codigo, nombre, direccion, telefono, camas))
        registros=cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros