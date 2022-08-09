from db.models import ClinicModel
import pymysql

def get_clinic_models(result: tuple) -> dict:
    result = list(result)
    result.sort(key= lambda x: int(x[0]))
    clinic_models = list()
    for result_tuple in result:
        clinic_model = ClinicModel()
        clinic_model.clinic_no = result_tuple[0]
        clinic_model.trial = result_tuple[1]
        clinic_model.city = result_tuple[2]
        clinic_model.name = result_tuple[3]
        clinic_model.ntc = bool(result_tuple[4])
        clinic_model.rat = bool(result_tuple[5])
        clinic_model.working_weekday = result_tuple[6]
        clinic_model.working_saturday = result_tuple[7]
        clinic_model.working_sunday= result_tuple[8]
        clinic_model.working_holiday = result_tuple[9]
        clinic_model.call = result_tuple[10]
        clinic_model.location = result_tuple[11]
        clinic_model.competent_name = result_tuple[12]
        clinic_model.competent_call = result_tuple[13]
        clinic_model.description = result_tuple[14]
        clinic_model.congestion = result_tuple[15]
        clinic_models.append(clinic_model)
    return clinic_models

def load_all_items(connection: pymysql.connections.Connection) -> dict:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM clinic;")
    clinic_models = get_clinic_models(cursor.fetchall())
    return clinic_models

def load_items_with_search(connection: pymysql.connections.Connection, search_values: dict) -> dict:
    cursor = connection.cursor()
    sql = "SELECT * FROM clinic WHERE "
    for key in search_values.keys():
        if type(search_values[key]) == bool:
            search_values[key] = int(search_values[key])
        if "working" not in key:
            sql += f"{key} IN ('{search_values[key]}')"
        else:
            if search_values[key] == 1:
                sql += f"{key}!='미운영'"
            else:
                sql += f"{key}='미운영'"
        if key != list(search_values)[-1]:
            sql += " AND "

    sql += ";"
    cursor.execute(sql)
    clinic_models = get_clinic_models(cursor.fetchall())
    return clinic_models


def insert_clinic_item(connection: pymysql.connections.Connection, clinic_item:ClinicModel) -> None:
    cursor = connection.cursor()
    try:
        cursor.execute(f"INSERT INTO clinic VALUES ('{clinic_item.clinic_no}', '{clinic_item.trial}', '{clinic_item.city}', '{clinic_item.name}', {clinic_item.ntc}, {clinic_item.rat}, '{clinic_item.working_weekday}', '{clinic_item.working_saturday}', '{clinic_item.working_sunday}', '{clinic_item.working_holiday}', '{clinic_item.call}', '{clinic_item.location}', '{clinic_item.competent_name}', '{clinic_item.competent_call}', '{clinic_item.description}', '{clinic_item.congestion}')")
        connection.commit()
    except pymysql.err.Error:
        raise pymysql.err.Error