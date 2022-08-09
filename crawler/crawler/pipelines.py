# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from db.connection import connect_db
from db.models import ClinicModel
from db.clinic import insert_clinic_item


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
