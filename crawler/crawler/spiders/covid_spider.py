from scrapy import Request
from scrapy.spiders import Spider
import datetime
import os

from ..items import CovidItem

class CovidSpider(Spider):
    name = "covid"
    covid_url = "https://sgis.kostat.go.kr/ServiceAPI/thematicMap/GetThemaMapData.json?thema_map_data_id=covid19_status&area_type=auto&adm_cd=00&covid_year_val={}&covid_month_val={}&covid_day_val={}"
    file_path = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))
    start_date = datetime.datetime.strptime("2020-03-01", "%Y-%m-%d")
    custom_settings = {
        'LOG_LEVEL': 'INFO',
        'LOG_FILE': 'crawler/spider.log',
        'ITEM_PIPELINES': {
            'crawler.crawler.pipelines.CovidPipeline': 100
        }
    }
    
    def start_requests(self):
        
        now = datetime.datetime.now()
        if os.path.isfile(f"{self.file_path}/setting"):
            
            f = open(f"{self.file_path}/last_date", 'r')
            date = datetime.datetime.strptime(f.readline(), "%Y-%m-%d")
            while date < now:
                request_url = self.covid_url.format(date.year, str(date.month).rjust(2, "0"), str(date.day).rjust(2, "0"))
                date += datetime.timedelta(days=1)
                yield Request(url = request_url, callback=self.load_items, headers={
                    "datetime": (date - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
                })
            
        else:
            
            date = self.start_date
            while date < now:
                request_url = self.covid_url.format(date.year, str(date.month).rjust(2, "0"), str(date.day).rjust(2, "0"))
                date += datetime.timedelta(days=1)
                yield Request(url = request_url, callback=self.load_items, headers={
                    "datetime": (date - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
                })

    def load_items(self, response):
        
        detail_info = response.json()["result"]["detailInfo"]

        covid_item = CovidItem()
        covid_item["date"] = datetime.datetime.strptime(str(response.request.headers["datetime"])[2:-1], "%Y-%m-%d")
        adm_cd_list = "00 11 21 22 23 24 25 26 29 31 32 33 34 35 36 37 38 39 99".split(" ")
        for index in range(len(detail_info)):
            covid_item[f"adm_cd_{adm_cd_list[index]}"] = detail_info[index]["left_data_val"]
            covid_item[f"adm_cd_{adm_cd_list[index]}_total"] = detail_info[index]["right_data_val"]

        yield covid_item
