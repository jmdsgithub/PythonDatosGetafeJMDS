import pyodbc

connection=pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost;DATABASE=HOSPITAL;UID=SA;PWD=Getafe12345@@;TrustServerCertificate=yes')

#connectionString = (f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={localhost};DATABASE={HOSPITAL};UID={SA};PWD={Getafe12345@@@})

Print('Conectado!!!')