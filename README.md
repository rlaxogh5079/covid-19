# 코로나바이러스19 API

이 서비스는 한국에 존재하는 선별진료소의 위치와 운영시간, 한국에서 발생하는 각 지역별 코로나 확진자들과 관련된 정보를 가공해 API를 제공하는 서비스입니다.

<hr />

### 사용법(WSL)

```bash
$ cd ~
$ git clone https://github.com/rlaxogh5079/covid-19
$ cd covid-19/crawler 
$ scrapy crawl clinic 
$ cd covid-19
$ python3 server.py
```


<hr />

### 선별진료소 확인

<b>request</b>
```json
    "clinic_no" : "선별진료소 고유 번호"
    "trial" : "대한민국 시도"
    "city": "대한민국 시군구"
    "name": "선별진료소 이름"
    "rat": "신속항원검사 여부"
    "working_weekday": "평일 운영 여부"
    "working_saturday": "토요일 운영 여부"
    "working_sunday": "일요일 운영 여부"
    "working_holiday": "공휴일 운영 여부"
    "competent_name": "관할보건소 이름"
```
trial의 리스트 : [서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주]

rat, working_weekday, working_saturday, working_sunday, working_holiday는 boolean 요소,
0: 거짓, 1: 참

<b>response</b>
```json
[
    {
        "clinic_no" : "선별진료소 고유 번호"
        "trial": "대한민국 시도"
        "city": "대한민국 시군구"
        "name": "선별진료소 이름"
        "ntc": "검체채취 가능 여부"
        "rat": "신속항원검사 여부"
        "working_weekday": "평일 운영 여부"
        "working_saturday": "토요일 운영 여부"
        "working_sunday": "일요일 운영 여부"
        "working_holiday": "공휴일 운영 여부"
        "call": "선별진료소 전화번호"
        "location": "선별진료소 위치"
        "competent_name": "관할보건소 이름"
        "competent_call": "관할보건소 전화번호"
        "description": "장애인편의사항"
        "congestion": "혼잡도"
    }
]
```

예시)
request
```
http://localhost:8000/clinics?clinic_no=123
```

response
```json
[
    {
        "clinic_no": "123",
        "trial": "대구",
        "city": "서구",
        "name": "대구의료원",
        "ntc": true,
        "rat": false,
        "working_weekday": "08:30~17:30 (소독)12:30~13:30",
        "working_saturday": "08:30~17:30 (소독)12:30~13:30",
        "working_sunday": "08:30~17:30 (소독)12:30~13:30",
        "working_holiday": "08:30~17:30 (소독)12:30~13:30",
        "call": "053-560-7575",
        "location": "대구 서구 평리로 157",
        "competent_name": "대구광역시 서구보건소",
        "competent_call": "053-663-3223",
        "description": "제공하지 않음",
        "congestion": "제공하지 않음"
    }
]
```

request
```
http://localhost:8000/clinics?trial=대전&city=대덕구&working_sunday=1
```


response
```json
[
    {
        "clinic_no": "167",
        "trial": "대전",
        "city": "대덕구",
        "name": "대덕구보건소",
        "ntc": true,
        "rat": false,
        "working_weekday": "09:00~11:30,13:30~18:00",
        "working_saturday": "09:00~11:30",
        "working_sunday": "09:00~11:30",
        "working_holiday": "09:00~11:30",
        "call": "042-608-4451~4455",
        "location": "대전 대덕구 석봉로38번길 55",
        "competent_name": "대덕구보건소",
        "competent_call": "042-608-5431",
        "description": "예약가능, 장애인 우선검사 실시",
        "congestion": "제공하지 않음"
    }
]
```
(미완)