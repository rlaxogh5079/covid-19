# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from db.connection import connect_db
from db.models import ClinicModel, CovidModel
from db.clinic import insert_clinic_item
from db.covid import insert_covid_item


class ClinicPipeline(object):
    def process_item(self, item, spider):
        connection = connect_db()
        model = ClinicModel()
        if item["description"] == None:
            item["description"] = "제공하지 않음"
        if item["congestion"] == None:
            item["congestion"] = "제공하지 않음"

        if item["clinic_sample"] == None:
            item["clinic_sample"] = False
        else:
            item["clinic_sample"] = True
        if item["clinic_RAT"] == None:
            item["clinic_RAT"] = False
        else:
            item["clinic_RAT"] = True

        model.clinic_no = item["clinic_no"]
        model.trial = item["clinic_trial"]
        model.city = item["clinic_city"]
        model.name = item["clinic_name"]
        model.ntc = item["clinic_sample"]
        model.rat = item["clinic_RAT"]
        model.working_weekday = item["clinic_time"]["weekday"]
        model.working_saturday = item["clinic_time"]["saturday"]
        model.working_sunday = item["clinic_time"]["sunday"]
        model.working_holiday = item["clinic_time"]["holiday"]
        model.call = item["clinic_call"]
        model.location = item["clinic_location"]
        model.competent_name = item["competent_clinic"]
        model.competent_call = item["competent_clinic_call"]
        model.description = item["description"]
        model.congestion = item["congestion"]
        insert_clinic_item(connection, model)

class CovidPipeline(object):
    def process_item(self, item, spider):
        connection = connect_db()
        model = CovidModel()

        model.date = item["date"]
        model.adm_cd_00 = str(item["adm_cd_00"])
        model.adm_cd_11 = str(item["adm_cd_11"])
        model.adm_cd_21 = str(item["adm_cd_21"])
        model.adm_cd_22 = str(item["adm_cd_22"])
        model.adm_cd_23 = str(item["adm_cd_23"])
        model.adm_cd_24 = str(item["adm_cd_24"])
        model.adm_cd_25 = str(item["adm_cd_25"])
        model.adm_cd_26 = str(item["adm_cd_26"])
        model.adm_cd_29 = str(item["adm_cd_29"])
        model.adm_cd_31 = str(item["adm_cd_31"])
        model.adm_cd_32 = str(item["adm_cd_32"])
        model.adm_cd_33 = str(item["adm_cd_33"])
        model.adm_cd_34 = str(item["adm_cd_34"])
        model.adm_cd_35 = str(item["adm_cd_35"])
        model.adm_cd_36 = str(item["adm_cd_36"])
        model.adm_cd_37 = str(item["adm_cd_37"])
        model.adm_cd_38 = str(item["adm_cd_38"])
        model.adm_cd_39 = str(item["adm_cd_39"])
        model.adm_cd_99 = str(item["adm_cd_99"])
        model.adm_cd_00_total= str(item["adm_cd_00_total"])
        model.adm_cd_11_total= str(item["adm_cd_11_total"])
        model.adm_cd_21_total= str(item["adm_cd_21_total"])
        model.adm_cd_22_total= str(item["adm_cd_22_total"])
        model.adm_cd_23_total= str(item["adm_cd_23_total"])
        model.adm_cd_24_total= str(item["adm_cd_24_total"])
        model.adm_cd_25_total= str(item["adm_cd_25_total"])
        model.adm_cd_26_total= str(item["adm_cd_26_total"])
        model.adm_cd_29_total= str(item["adm_cd_29_total"])
        model.adm_cd_31_total= str(item["adm_cd_31_total"])
        model.adm_cd_32_total= str(item["adm_cd_32_total"])
        model.adm_cd_33_total= str(item["adm_cd_33_total"])
        model.adm_cd_34_total= str(item["adm_cd_34_total"])
        model.adm_cd_35_total= str(item["adm_cd_35_total"])
        model.adm_cd_36_total= str(item["adm_cd_36_total"])
        model.adm_cd_37_total= str(item["adm_cd_37_total"])
        model.adm_cd_38_total= str(item["adm_cd_38_total"])
        model.adm_cd_39_total= str(item["adm_cd_39_total"])
        model.adm_cd_99_total= str(item["adm_cd_99_total"])
        insert_covid_item(connection, model)