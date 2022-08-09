from db.setting import create_database, create_clinic_table, create_covid_table
import pymysql

connect_data = {
    "host": "localhost",
    "user": "user", # insert your mysql id
    "password": "password", # insert your mysql password
}

def connect_db() -> pymysql.connections.Connection:
    try:
        conn = pymysql.connect(
        host=connect_data["host"],
        user=connect_data["user"],
        password=connect_data["password"],
    )   
        flag = create_database(conn)
        conn.select_db("covid_19")
        if flag:
            create_clinic_table(conn)
            create_covid_table(conn)
        return conn
    except pymysql.err.Error:
        raise pymysql.err.Error
