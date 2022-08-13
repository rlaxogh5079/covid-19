from scrapy import Request
from scrapy.spiders import Spider
from ..items import ClinicItem
from selenium import webdriver, common
import re
import os

class ClinicSpider(Spider):
    name = "clinic"
    clinic_url = "https://www.mohw.go.kr/react/ncov/selclinic04ls.jsp?page={}&SEARCHVALUE="
    start_url = clinic_url.format(1)
    custom_settings = {
        'LOG_LEVEL': 'INFO',
        'LOG_FILE': 'crawler/spider.log',
        'ITEM_PIPELINES': {
            'crawler.crawler.pipelines.ClinicPipeline': 100
        }
    }
    
    def start_requests(self):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        self.driver = webdriver.Chrome(executable_path = f"{os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))}/chromedriver", options=options)
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

            clinic_item["clinic_no"] = tr[idx].xpath("th/text()").get()
            clinic_item["clinic_trial"] = tr[idx].xpath("td[1]/text()").get()
            clinic_item["clinic_city"] = tr[idx].xpath("td[2]/text()").get()
            clinic_item["clinic_name"] = tr[idx].xpath(
                "td[3]/strong/text()").get()
            clinic_item["clinic_sample"] = tr[idx].xpath(
                "td[3]/strong/i[@class='ico_ntc']/span/text()").get()
            clinic_item["clinic_RAT"] = tr[idx].xpath(
                "td[3]/strong/i[@class='ico_rat']/span/text()").get()
            clinic_item["clinic_time"] = clinic_time
            clinic_item["clinic_call"] = tr[idx].xpath("td[4]/a/text()").get()
            clinic_item["competent_clinic"] = tr[idx].xpath(
                "td[6]/text()").get()
            clinic_item["competent_clinic_call"] = tr[idx].xpath(
                "td[7]/a/text()").get()
            clinic_item["description"] = tr[idx].xpath("td[8]/text()").get()
            clinic_item["congestion"] = tr[idx].xpath("td[9]/text()").get()

            try:
                request_url = "https://www.mohw.go.kr" + tr[idx].xpath("td[5]/a/@href").get()
                self.driver.get(request_url)
                self.driver.implicitly_wait(time_to_wait=5)
                html = self.driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div[1]/div/div[6]/div[2]/div/div[1]/span[1]").text
                clinic_item["clinic_location"] = html
                
                yield clinic_item
            except common.exceptions.NoSuchElementException:
                clinic_item["clinic_location"] = "지도를 지원하지 않음"
                yield clinic_item
            