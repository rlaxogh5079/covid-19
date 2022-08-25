from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from db.clinic import load_all_clinic_items, load_clinic_items_with_search, drop_clinic_items
from db.covid import  load_all_covid_items,  load_covid_items_with_search, insert_last_date
from db.connection import connect_db
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from crawler.crawler.spiders.clinic_spider import ClinicSpider
from crawler.crawler.spiders.covid_spider import CovidSpider
import os
import uvicorn
import datetime

tags_metadata = [
    {
        "name": "clinic",
        "description": "코로나바이러스19의 선별진료소와 관련된 태그",
    },
    {
        "name": "covid",
        "description": "코로나바이러스19 확진자와 관련된 태그",
    },
]

app = FastAPI(
    title="covid-19",
    description="코로나바이러스19와 관련된 정보들을 API로 제공하는 서비스",
    version="0.0.1",
    terms_of_service=None,
    contact={
        "name": "Developer",
        "email": "rlaxogh507906@gmail.com"
    },
    openapi_tags=tags_metadata,
    openapi_url="/docs/json"
    )

conn = connect_db()

def crawler_run() -> None:
    runner = CrawlerRunner()
    runner.crawl(ClinicSpider)
    runner.crawl(CovidSpider)
    d = runner.join()
    d.addBoth(lambda _ : reactor.stop())
    reactor.run()

def setting() -> None:
    print("setting server...")
    crawler_run()
    print("end setting")
    f = open(f"{file_path}/setting", "w")
    f.write("This file is for checking whether it is set or not")
    f.close()

@app.on_event('startup')
@repeat_every(seconds=1)
async def startup():
    now = datetime.datetime.now()
    if now.hour == 0 and now.minute == 0 and now.second == 0:
        drop_clinic_items(conn)
        crawler_run()
        insert_last_date(conn)
        
    
@app.get("/clinics", tags=["clinic"])
async def clinics(clinic_no: str = None, trial: str = None, city: str = None, name: str = None, rat: bool = None, working_weekday: bool = None, working_saturday: bool = None, working_sunday: bool = None, working_holiday: bool = None, competent_name: str = None):
    if clinic_no == trial == city == name == rat == working_weekday == working_saturday == working_sunday == working_holiday == competent_name == None:
        return load_all_clinic_items(conn)

    else:
        search_values = dict()
        if clinic_no != None:
            search_values["clinic_no"] = clinic_no
        if trial != None:
            search_values["trial"] = trial
        if city != None:
            search_values["city"] = city
        if name != None:
            search_values["name"] = name
        if rat != None:
            search_values["rat"] = rat
        if working_weekday != None:
            search_values["working_weekday"] = working_weekday
        if working_saturday != None:
            search_values["working_saturday"] = working_saturday
        if working_sunday != None:
            search_values["working_sunday"] = working_sunday
        if working_holiday != None:
            search_values["working_holiday"] = working_holiday
        if competent_name != None:
            search_values["competent_name"] = competent_name

        return load_clinic_items_with_search(conn, search_values)

@app.get("/covids", tags=["covid"])
async def covids(date: str = None, adm_cd_no:str = None):
    if date == adm_cd_no == None:
        return load_all_covid_items(conn)

    search_values = dict()
    if date != None:
        search_values["date"] = date
    if adm_cd_no != None:
        search_values["adm_cd_no"] = adm_cd_no
    
    return load_covid_items_with_search(conn, search_values)


if __name__ == "__main__":
    file_path = os.path.abspath(os.path.dirname(__file__))
    if not os.path.isfile(f"{file_path}/setting"):
        setting()
    
    uvicorn.run(app="server:app", host="localhost", port=8000, reload=True)

