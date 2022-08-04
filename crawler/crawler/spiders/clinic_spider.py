from scrapy import Request
from scrapy.spiders import Spider
from ..items import ClinicItem
import requests
import json
import re


class ClinicSpider(Spider):
    name = "clinic"
    clinic_url = "https://www.mohw.go.kr/react/ncov/selclinic04ls.jsp?page={}&SEARCHVALUE="
    start_url = clinic_url.format(1)

    def start_requests(self):
        yield Request(url=self.start_url, callback=self.load_pages)

    def load_pages(self, response):
        js_code = response.xpath("/html/body/div[2]/div[2]/script").get()
        js_total_cnt = re.findall(r"var nTotalCnt = \"\d{0,9}\"", js_code)[0]
        total_cnt = int(js_total_cnt.split("=")[1].replace("\"", ""))
        page_length = int(total_cnt / 20) + 1

        for page in range(page_length):
            request_url = self.clinic_url.format(page + 1)
            yield Request(url=request_url, callback=self.load_items, dont_filter=True)

    def load_items(self, response):
        clinic_item = ClinicItem()
        tr = response.xpath(
            "/html/body/div[2]/div[2]/div[7]/table/tbody/tr")

        for idx in range(len(tr)):
            clinic_time = dict()
            clinic_time["weekday"] = tr[idx].xpath(
                "td[3]/p/span[1]/text()").get()
            clinic_time["saturday"] = tr[idx].xpath(
                "td[3]/p/span[2]/text()").get()
            clinic_time["sunday"] = tr[idx].xpath(
                "td[3]/p/span[3]/text()").get()
            clinic_time["holiday"] = tr[idx].xpath(
                "td[3]/p/span[4]/text()").get()

            clinic_item["clinic_no"] = int(tr[idx].xpath("th/text()").get())
            clinic_item["clinic_trial"] = tr[idx].xpath("td[1]/text()").get()
            clinic_item["clinic_city"] = tr[idx].xpath("td[2]/text()").get()
            clinic_item["clinic_name"] = tr[idx].xpath(
                "td[3]/strong/text()").get()
            clinic_item["clinic_sample"] = tr[idx].xpath(
                "td[3]/strong/i[@class='ico_ntc']/text()").get()
            clinic_item["clinic_RAT"] = tr[idx].xpath(
                "td[3]/strong/i[@class='ico_rat']/text()").get()
            clinic_item["clinic_time"] = clinic_time
            clinic_item["clinic_call"] = tr[idx].xpath("td[4]/a/text()").get()
            clinic_item["competent_clinic"] = tr[idx].xpath(
                "td[6]/text()").get()
            clinic_item["competent_clinic_call"] = tr[idx].xpath(
                "td[7]/a/text()").get()
            clinic_item["description"] = tr[idx].xpath("td[8]/text()").get()
            clinic_item["congestion"] = tr[idx].xpath("td[9]/text()").get()

            request_query = f'{clinic_item["clinic_trial"]} {clinic_item["clinic_trial"]} 선별진료소 {clinic_item["clinic_name"]}'
            request_url = "https://dapi.kakao.com/v2/local/search/keyword.json?query=" + request_query

            clinic_item["clinic_location"] = json.loads(requests.get(request_url, headers={
                "Origin": "https://www.mohw.go.kr",
                "Referer": "https://www.mohw.go.kr/",
                "Authorization": "KakaoAK 0a229229b783e6330fc2e6e9a459c730",
                "KA": "sdk/4.4.6-fixed2 os/javascript lang/ko-KR device/Win32 origin/https%3A%2F%2Fwww.mohw.go.kr"
            }).text)["documents"][0]["address_name"]

            yield clinic_item
