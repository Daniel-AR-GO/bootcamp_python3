import sqlite3
base = sqlite3.connect('acciones_datos.db')
cursor = base.cursor()

cursor.execute('CREATE TABLE socios(Nombre TEXT, Acciones INT, Efectivo REAL, Fecha TEXT)')
cursor.execute('INSERT INTO socios VALUES("Daniel", 1000, 10000.00, "2018-12-12")')
cursor.execute('INSERT INTO socios VALUES("Lilo", 1000, 12000.00, "2017-11-14")')
cursor.execute('INSERT INTO socios VALUES("Robin", 2000, 40000.00, "2018-01-20")')
cursor.execute('INSERT INTO socios VALUES("Mila", 2000, 40000.00, "2018-03-20")')
base.commit()
base.close()