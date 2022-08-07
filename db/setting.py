import pymysql


def create_database(connection: pymysql.connections.Connection) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE covid_19")
        return True
    except pymysql.err.Error:
        return False

def create_clinic_table(connection: pymysql.connections.Connection) -> None:
    try:
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE clinic(
            `clinic_no` VARCHAR(5) NOT NULL PRIMARY KEY,
            `trial` TEXT NOT NULL,
            `city` TEXT NOT NULL,
            `name` TEXT NOT NULL,
            `ntc` BOOLEAN DEFAULT false,
            `rat` BOOLEAN DEFAULT false,
            `working_weekday` TEXT NOT NULL,
            `working_saturday` TEXT NOT NULL,
            `working_sunday` TEXT NOT NULL,
            `working_holiday` TEXT NOT NULL,
            `call` TEXT NOT NULL,
            `location` TEXT NOT NULL,
            `competent_name` TEXT NOT NULL,
            `competent_call` TEXT NOT NULL,
            `description` TEXT NOT NULL,
            `congestion` TEXT NOT NULL
            );""")
    except pymysql.err.Error:
        raise pymysql.err.Error