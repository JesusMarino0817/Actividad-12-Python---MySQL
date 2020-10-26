import mysql.connector

bd = mysql.connector.connect(user='jesus', password='Jm0817',
database='nopalitos')

cursor = bd.cursor()

while True:
    print('1) agregar usuario')
    print('2) Mostrar usuario')
    print('0) Salir')
    op = input()

    if op == '1':
        correo = input('correo:')
        contra = input('contraseña:')

        consulta = "INSERT INTO usuarios (correo, contrasena)" "VALUES (%s, %s)"

        cursor.execute(consulta, (correo, contra))
        bd.commit()
        if cursor.rowcount:
            print('Se agrego usuario')
        else:
            print('Error')

    elif op =='2':
        consulta = "SELECT * FROM usuarios"

        cursor.execute(consulta)
        for row in cursor.fetchall():
            print('Id: ', row[0])
            print('Correo: ', row[2])
            print('Contraseña: ', row[1])
    elif op == '0':
        break