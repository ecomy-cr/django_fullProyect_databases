import mysql.connector 
from os import environ
from dotenv import load_dotenv
load_dotenv()

host_db = environ.get('DB_HOST')
db_db = environ.get('DB_NAME')
user_db = environ.get('DB_USER')
password_db = environ.get('DB_PASSWORD')

def mirar_db(namet):
    try:
        mi_base_datos_directo = mysql.connector.connect(host=host_db, user= user_db, password=password_db, database=db_db)

        mycur = mi_base_datos_directo.cursor()
        query="show tables"
        mycur.execute(query)

        for i in mycur:
            print(i)

        mycur = mi_base_datos_directo.cursor()
        query=f"select * from {namet}"

        mycur.execute(query)
        datos = mycur.fetchall()

        return datos

    except Exception as e:
        print(str(e))

