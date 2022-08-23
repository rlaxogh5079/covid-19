from db.models import CovidModel
import os
import pymysql

def get_covid_model_all(result: tuple) -> list:
    result = list(result)
    covid_models = list()
    for result_tuple in result:
        covid_model = CovidModel()
        covid_model.date = result_tuple[0].strftime("%Y-%m-%d")
        covid_model.adm_cd_00 = result_tuple[1]
        covid_model.adm_cd_11 = result_tuple[2]
        covid_model.adm_cd_21 = result_tuple[3]
        covid_model.adm_cd_22 = result_tuple[4]
        covid_model.adm_cd_23 = result_tuple[5]
        covid_model.adm_cd_24 = result_tuple[6]
        covid_model.adm_cd_25 = result_tuple[7]
        covid_model.adm_cd_26 = result_tuple[8]
        covid_model.adm_cd_29 = result_tuple[9]
        covid_model.adm_cd_31 = result_tuple[10]
        covid_model.adm_cd_32 = result_tuple[11]
        covid_model.adm_cd_33 = result_tuple[12]
        covid_model.adm_cd_34 = result_tuple[13]
        covid_model.adm_cd_35 = result_tuple[14]
        covid_model.adm_cd_36 = result_tuple[15]
        covid_model.adm_cd_37 = result_tuple[16]
        covid_model.adm_cd_38 = result_tuple[17]
        covid_model.adm_cd_39 = result_tuple[18]
        covid_model.adm_cd_99 = result_tuple[19]
        covid_model.adm_cd_00_total = result_tuple[20]
        covid_model.adm_cd_11_total = result_tuple[21]
        covid_model.adm_cd_21_total = result_tuple[22]
        covid_model.adm_cd_22_total = result_tuple[23]
        covid_model.adm_cd_23_total = result_tuple[24]
        covid_model.adm_cd_24_total = result_tuple[25]
        covid_model.adm_cd_25_total = result_tuple[26]
        covid_model.adm_cd_26_total = result_tuple[27]
        covid_model.adm_cd_29_total = result_tuple[28]
        covid_model.adm_cd_31_total = result_tuple[29]
        covid_model.adm_cd_32_total = result_tuple[30]
        covid_model.adm_cd_33_total = result_tuple[31]
        covid_model.adm_cd_34_total = result_tuple[32]
        covid_model.adm_cd_35_total = result_tuple[33]
        covid_model.adm_cd_36_total = result_tuple[34]
        covid_model.adm_cd_37_total = result_tuple[35]
        covid_model.adm_cd_38_total = result_tuple[36]
        covid_model.adm_cd_39_total = result_tuple[37]
        covid_model.adm_cd_99_total = result_tuple[38]
        covid_models.append(covid_model)
    return covid_models

def get_covid_model(result: tuple, adm_cd_no: str) -> list:
    result = list(result)
    covid_models = list()
    for result_tuple in result:
        covid_model = dict()
        covid_model["date"] = result_tuple[0]
        covid_model[f"adm_cd_{adm_cd_no}"] = result_tuple[1]
        covid_model[f"adm_cd_{adm_cd_no}_total"] = result_tuple[2]
        covid_models.append(covid_model)
    
    return covid_models


def load_all_covid_items(connection: pymysql.connections.Connection) -> list:
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM covid")
        result = cursor.fetchall()
        models = get_covid_model_all(result)
        return models
    except pymysql.err.Error:
        raise pymysql.err.Error


def load_covid_items_with_search(connection: pymysql.connections.Connection, search_values: dict) -> list:
    cursor = connection.cursor()
    if "adm_cd_no" not in search_values.keys():
        date = search_values["date"]
        cursor.execute(f"SELECT * FROM covid WHERE date='{date}';")
        result = cursor.fetchall()
        models = get_covid_model_all(result)
        return models
    else:
        adm_cd_no = search_values["adm_cd_no"]
        sql = f"SELECT date, adm_cd_{adm_cd_no}, adm_cd_{adm_cd_no}_total FROM covid"
        if "date" in search_values.keys():
            date = search_values["date"]
            sql += f" WHERE date='{date}'"
        sql += ";"
        cursor.execute(sql)
        result = cursor.fetchall()
        models = get_covid_model(result, adm_cd_no)

        return models


def insert_covid_item(connection: pymysql.connections.Connection, covid_item: CovidModel) -> None:
    cursor = connection.cursor()
    try:
        cursor.execute(f"INSERT INTO covid VALUES ('{covid_item.date}', '{covid_item.adm_cd_00}', '{covid_item.adm_cd_11}', '{covid_item.adm_cd_21}', '{covid_item.adm_cd_22}', '{covid_item.adm_cd_23}', '{covid_item.adm_cd_24}', '{covid_item.adm_cd_25}', '{covid_item.adm_cd_26}', '{covid_item.adm_cd_29}', '{covid_item.adm_cd_31}', '{covid_item.adm_cd_32}', '{covid_item.adm_cd_33}', '{covid_item.adm_cd_34}', '{covid_item.adm_cd_35}', '{covid_item.adm_cd_36}', '{covid_item.adm_cd_37}', '{covid_item.adm_cd_38}', '{covid_item.adm_cd_39}', '{covid_item.adm_cd_99}', '{covid_item.adm_cd_00_total}', '{covid_item.adm_cd_11_total}', '{covid_item.adm_cd_21_total}', '{covid_item.adm_cd_22_total}', '{covid_item.adm_cd_23_total}', '{covid_item.adm_cd_24_total}', '{covid_item.adm_cd_25_total}', '{covid_item.adm_cd_26_total}', '{covid_item.adm_cd_29_total}', '{covid_item.adm_cd_31_total}', '{covid_item.adm_cd_32_total}', '{covid_item.adm_cd_33_total}', '{covid_item.adm_cd_34_total}', '{covid_item.adm_cd_35_total}', '{covid_item.adm_cd_36_total}', '{covid_item.adm_cd_37_total}', '{covid_item.adm_cd_38_total}', '{covid_item.adm_cd_39_total}', '{covid_item.adm_cd_99_total}' );")
        connection.commit()
    except pymysql.err.Error:
        raise pymysql.err.Error


def load_last_date() -> str:
    file_path = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

    f = open(f"{file_path}/last_date", "r")
    last_date = f.readline()

    return last_date

def insert_last_date(connection: pymysql.connections.Connection) -> None:
    file_path = os.path.abspath(os.path.dirname(os.path.abspaht(os.path.dirname(__file__))))
    cursor = connection.cursor()

    cursor.execute(f"SELECT date FROM covid ORDER BY date DESC LIMIT 1;")
    result = cursor.fetchall()

    f = open(f"{file_path}/last_date", "w")
    f.write(result[0][0].strftime("%Y-%m-%d"))
    f.close()