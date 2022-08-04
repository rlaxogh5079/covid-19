from scrapy import Item, Field


class ClinicItem(Item):
    clinic_no = Field()  # 연번
    clinic_trial = Field()  # 시도
    clinic_city = Field()  # 시군구
    clinic_name = Field()  # 선별진료소 이름
    clinic_sample = Field()  # 검체채취 가능
    clinic_RAT = Field()  # 신속 항원 검사 가능
    clinic_time = Field()  # 운영시간
    clinic_call = Field()  # 전화번호
    clinic_location = Field()  # 위치
    competent_clinic = Field()  # 관할보건소
    competent_clinic_call = Field()  # 관할보건소 전화번호
    description = Field()  # 장애인 편의사항
    congestion = Field()  # 혼잡도
