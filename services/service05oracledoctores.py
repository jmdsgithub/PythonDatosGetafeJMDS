import oracledb
from models import doctor as model

class ServiceOracleDoctores:
    def __init__(self):
        self.connection=oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

    def getAllDoctores(self):
        sql='select * from DOCTOR'
        cursor=self.connection.cursor()
        cursor.execute(sql)
        datos=[]
        for row in cursor:
            doc=model.Doctor()
            doc.idDoctor=row[1]
            doc.apellido=row[2]
            doc.especialidad=row[3]
            doc.salario=row[4]
            doc.hospital=row[0]
            datos.append(doc)
        cursor.close()
        return datos


