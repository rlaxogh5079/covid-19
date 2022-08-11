from db.models import CovidModel
import pymysql

def insert_covid_item(connection: pymysql.connections.Connection, covid_item: CovidModel) -> None:
    cursor = connection.cursor()
    try:
        cursor.execute(f"INSERT INTO covid VALUES ('{covid_item.date}', '{covid_item.adm_cd_00}', '{covid_item.adm_cd_11}', '{covid_item.adm_cd_21}', '{covid_item.adm_cd_22}', '{covid_item.adm_cd_23}', '{covid_item.adm_cd_24}', '{covid_item.adm_cd_25}', '{covid_item.adm_cd_26}', '{covid_item.adm_cd_29}', '{covid_item.adm_cd_31}', '{covid_item.adm_cd_32}', '{covid_item.adm_cd_33}', '{covid_item.adm_cd_34}', '{covid_item.adm_cd_35}', '{covid_item.adm_cd_36}', '{covid_item.adm_cd_37}', '{covid_item.adm_cd_38}', '{covid_item.adm_cd_39}', '{covid_item.adm_cd_99}', '{covid_item.adm_cd_00_total}', '{covid_item.adm_cd_11_total}', '{covid_item.adm_cd_21_total}', '{covid_item.adm_cd_22_total}', '{covid_item.adm_cd_23_total}', '{covid_item.adm_cd_24_total}', '{covid_item.adm_cd_25_total}', '{covid_item.adm_cd_26_total}', '{covid_item.adm_cd_29_total}', '{covid_item.adm_cd_31_total}', '{covid_item.adm_cd_32_total}', '{covid_item.adm_cd_33_total}', '{covid_item.adm_cd_34_total}', '{covid_item.adm_cd_35_total}', '{covid_item.adm_cd_36_total}', '{covid_item.adm_cd_37_total}', '{covid_item.adm_cd_38_total}', '{covid_item.adm_cd_39_total}', '{covid_item.adm_cd_99_total}' );")
        connection.commit()
    except pymysql.err.Error:
        raise pymysql.err.Error