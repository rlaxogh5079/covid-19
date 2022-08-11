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

def create_covid_table(connection: pymysql.connections.Connection) -> None:

    try:    
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE covid(
            `date` DATETIME NOT NULL PRIMARY KEY,
            `adm_cd_00` TEXT NOT NULL,
            `adm_cd_11` TEXT NOT NULL,
            `adm_cd_21` TEXT NOT NULL,
            `adm_cd_22` TEXT NOT NULL,
            `adm_cd_23` TEXT NOT NULL,
            `adm_cd_24` TEXT NOT NULL,
            `adm_cd_25` TEXT NOT NULL,
            `adm_cd_26` TEXT NOT NULL,
            `adm_cd_29` TEXT NOT NULL,
            `adm_cd_31` TEXT NOT NULL,
            `adm_cd_32` TEXT NOT NULL,
            `adm_cd_33` TEXT NOT NULL,
            `adm_cd_34` TEXT NOT NULL,
            `adm_cd_35` TEXT NOT NULL,
            `adm_cd_36` TEXT NOT NULL,
            `adm_cd_37` TEXT NOT NULL,
            `adm_cd_38` TEXT NOT NULL,
            `adm_cd_39` TEXT NOT NULL,
            `adm_cd_99` TEXT NOT NULL,
            `adm_cd_00_total` TEXT NOT NULL,
            `adm_cd_11_total` TEXT NOT NULL,
            `adm_cd_21_total` TEXT NOT NULL,
            `adm_cd_22_total` TEXT NOT NULL,
            `adm_cd_23_total` TEXT NOT NULL,
            `adm_cd_24_total` TEXT NOT NULL,
            `adm_cd_25_total` TEXT NOT NULL,
            `adm_cd_26_total` TEXT NOT NULL,
            `adm_cd_29_total` TEXT NOT NULL,
            `adm_cd_31_total` TEXT NOT NULL,
            `adm_cd_32_total` TEXT NOT NULL,
            `adm_cd_33_total` TEXT NOT NULL,
            `adm_cd_34_total` TEXT NOT NULL,
            `adm_cd_35_total` TEXT NOT NULL,
            `adm_cd_36_total` TEXT NOT NULL,
            `adm_cd_37_total` TEXT NOT NULL,
            `adm_cd_38_total` TEXT NOT NULL,
            `adm_cd_39_total` TEXT NOT NULL,
            `adm_cd_99_total` TEXT NOT NULL
            );""")
    except pymysql.err.Error:
        raise pymysql.err.Error