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
            `adm_cd_sum` INT NOT NULL,
            `adm_cd_11` INT NOT NULL,
            `adm_cd_21` INT NOT NULL,
            `adm_cd_22` INT NOT NULL,
            `adm_cd_23` INT NOT NULL,
            `adm_cd_24` INT NOT NULL,
            `adm_cd_25` INT NOT NULL,
            `adm_cd_26` INT NOT NULL,
            `adm_cd_29` INT NOT NULL,
            `adm_cd_31` INT NOT NULL,
            `adm_cd_32` INT NOT NULL,
            `adm_cd_33` INT NOT NULL,
            `adm_cd_34` INT NOT NULL,
            `adm_cd_35` INT NOT NULL,
            `adm_cd_36` INT NOT NULL,
            `adm_cd_37` INT NOT NULL,
            `adm_cd_38` INT NOT NULL,
            `adm_cd_39` INT NOT NULL,
            `adm_cd_foreign` INT NOT NULL,
            `adm_cd_sum_total` INT NOT NULL,
            `adm_cd_11_total` INT NOT NULL,
            `adm_cd_21_total` INT NOT NULL,
            `adm_cd_22_total` INT NOT NULL,
            `adm_cd_23_total` INT NOT NULL,
            `adm_cd_24_total` INT NOT NULL,
            `adm_cd_25_total` INT NOT NULL,
            `adm_cd_26_total` INT NOT NULL,
            `adm_cd_29_total` INT NOT NULL,
            `adm_cd_31_total` INT NOT NULL,
            `adm_cd_32_total` INT NOT NULL,
            `adm_cd_33_total` INT NOT NULL,
            `adm_cd_34_total` INT NOT NULL,
            `adm_cd_35_total` INT NOT NULL,
            `adm_cd_36_total` INT NOT NULL,
            `adm_cd_37_total` INT NOT NULL,
            `adm_cd_38_total` INT NOT NULL,
            `adm_cd_39_total` INT NOT NULL,
            `adm_cd_foreign_total` INT NOT NULL
            );""")
    except pymysql.err.Error:
        raise pymysql.err.Error