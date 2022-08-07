from models import ClinicModel
import pymysql

def insert_item(connection: pymysql.connections.Connection, clinic_item:ClinicModel):
    cursor = connection.cursor()
    try:
        cursor.execute(f"INSERT INTO clinic VALUES ('{clinic_item.clinic_no}', '{clinic_item.trial}', '{clinic_item.city}', '{clinic_item.name}', {clinic_item.ntc}, {clinic_item.rat}, '{clinic_item.working_weekday}', '{clinic_item.working_saturday}', '{clinic_item.working_sunday}', '{clinic_item.working_holiday}', '{clinic_item.call}', '{clinic_item.location}', '{clinic_item.competent_name}', '{clinic_item.competent_call}', '{clinic_item.description}', '{clinic_item.congestion}')")
        connection.commit()
    except pymysql.err.Error:
        raise pymysql.err.Error