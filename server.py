from fastapi import FastAPI
from db.clinic import load_all_items, load_items_with_search
from db.connection import connect_db
import uvicorn

tags_metadata = [
    {
        "name": "clinic",
        "description": "코로나바이러스19의 선별진료소와 관련된 태그",
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

@app.get("/clinics", tags=["clinic"])
async def clinics(clinic_no: str = None, trial: str = None, city: str = None, name: str = None, rat: bool = None, working_weekday: bool = None, working_saturday: bool = None, working_sunday: bool = None, working_holiday: bool = None, competent_name: str = None):
    if clinic_no == trial == city == name == rat == working_weekday == working_saturday == working_sunday == working_holiday == competent_name == None:
        return load_all_items(conn)

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
        return load_items_with_search(conn, search_values)

if __name__ == "__main__":
    uvicorn.run(app="server:app", host="localhost", port=8000, reload=True)
