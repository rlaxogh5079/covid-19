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

class CovidItem(Item):
    date = Field() # 데이터 날짜
    adm_cd_00 = Field() # 일일 총 확진자수
    adm_cd_11 = Field() # 서울 총 확진자수
    adm_cd_21 = Field() # 부산 총 확진자수
    adm_cd_22 = Field() # 대구 총 확진자수
    adm_cd_23 = Field() # 인천 총 확진자수
    adm_cd_24 = Field() # 광주 총 확진자수
    adm_cd_25 = Field() # 대전 총 확진자수
    adm_cd_26 = Field() # 울산 총 확진자수
    adm_cd_29 = Field() # 세종 총 확진자수
    adm_cd_31 = Field() # 경기도 총 확진자수
    adm_cd_32 = Field() # 강원도 총 확진자수
    adm_cd_33 = Field() # 충청북도 총 확진자수
    adm_cd_34 = Field() # 충청남도 총 확진자수
    adm_cd_35 = Field() # 전라북도 총 확진자수
    adm_cd_36 = Field() # 전라남도 총 확진자수
    adm_cd_37 = Field() # 경상북도 총 확진자수
    adm_cd_38 = Field() # 경상남도 총 확진자수
    adm_cd_39 = Field() # 제주도 총 확진자수
    adm_cd_99 = Field() # 검열 총 확진자수
    adm_cd_00_total = Field() # 일일 전체기간 총 확진자수
    adm_cd_11_total = Field() # 서울 전체기간 총 확진자수
    adm_cd_21_total = Field() # 부산 전체기간 총 확진자수
    adm_cd_22_total = Field() # 대구 전체기간 총 확진자수
    adm_cd_23_total = Field() # 인천 전체기간 총 확진자수
    adm_cd_24_total = Field() # 광주 전체기간 총 확진자수
    adm_cd_25_total = Field() # 대전 전체기간 총 확진자수
    adm_cd_26_total = Field() # 울산 전체기간 총 확진자수
    adm_cd_29_total = Field() # 세종 전체기간 총 확진자수
    adm_cd_31_total = Field() # 경기도 전체기간 총 확진자수
    adm_cd_32_total = Field() # 강원도 전체기간 총 확진자수
    adm_cd_33_total = Field() # 충청북도 전체기간 총 확진자수
    adm_cd_34_total = Field() # 충청남도 전체기간 총 확진자수
    adm_cd_35_total = Field() # 전라북도 전체기간 총 확진자수
    adm_cd_36_total = Field() # 전라남도 전체기간 총 확진자수
    adm_cd_37_total = Field() # 경상북도 전체기간 총 확진자수
    adm_cd_38_total = Field() # 경산마도 전체기간 총 확진자수
    adm_cd_39_total = Field() # 제주도 전체기간 총 확진자수
    adm_cd_99_total = Field() # 검열 전체기간 총 확진자수
