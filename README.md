# 코로나바이러스19 API

이 서비스는 한국에 존재하는 선별진료소의 위치와 운영시간, 한국에서 발생하는 각 지역별 코로나 확진자들과 관련된 정보를 가공해 API를 제공하는 서비스입니다.

<hr />

### 사용법

```bash
$ cd ~
$ git clone https://github.com/rlaxogh5079/covid-19 
$ cd covid-19
$ python3 server.py
```


<hr />

### 선별진료소 확인

```
url : https://localhost:8000/clinics
```

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
        "clinic_no" : "선별진료소 고유 번호",
        "trial": "대한민국 시도",
        "city": "대한민국 시군구",
        "name": "선별진료소 이름",
        "ntc": "검체채취 가능 여부",
        "rat": "신속항원검사 여부",
        "working_weekday": "평일 운영 여부",
        "working_saturday": "토요일 운영 여부",
        "working_sunday": "일요일 운영 여부",
        "working_holiday": "공휴일 운영 여부",
        "call": "선별진료소 전화번호",
        "location": "선별진료소 위치",
        "competent_name": "관할보건소 이름",
        "competent_call": "관할보건소 전화번호",
        "description": "장애인편의사항",
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

### 코로나바이러스 확진자 확인

```
url : http://localhost:8000/covids
```

<b>request</b>

```json
    "date" : "날짜",
    "adm_cd_no" : "지역 고유 번호"
```

<b>response</b>

```json
    "adm_cd_no" : "일일 확진자",
    "adm_cd_no_total" : "누적 확진자"
```

```json
    "adm_cd_00" : "전체 지역 확진자",
    "adm_cd_11" : "서울 지역 확진자",
    "adm_cd_21" : "부산광역시 지역 확진자",
    "adm_cd_22" : "대구광역시 지역 확진자",
    "adm_cd_23" : "인천 지역 확진자",
    "adm_cd_24" : "광주광역시 지역 확진자",
    "adm_cd_25" : "대전광역시 지역 확진자",
    "adm_cd_26" : "울산광역시 지역 확진자",
    "adm_cd_29" : "세종시 지역 확진자",
    "adm_cd_31" : "경기도 지역 확진자",
    "adm_cd_32" : "강원도 지역 확진자",
    "adm_cd_33" : "충청북도 지역 확진자",
    "adm_cd_34" : "충청남도 지역 확진자",
    "adm_cd_35" : "전라북도 지역 확진자",
    "adm_cd_36" : "전라남도 지역 확진자",
    "adm_cd_37" : "경상북도 지역 확진자",
    "adm_cd_38" : "경상남도 지역 확진자",
    "adm_cd_39" : "제주도 지역 확진자",
    "adm_cd_99" : "해외 유입 확진자",
```


예시)
request
```
http://localhost:8000/covids?date=2022-02-02
```

response

```json
[
    {
        "date": "2022-02-02",
        "adm_cd_00": "20270",
        "adm_cd_11": "4209",
        "adm_cd_21": "1267",
        "adm_cd_22": "1147",
        "adm_cd_23": "1400",
        "adm_cd_24": "618",
        "adm_cd_25": "481",
        "adm_cd_26": "300",
        "adm_cd_29": "140",
        "adm_cd_31": "6050",
        "adm_cd_32": "354",
        "adm_cd_33": "459",
        "adm_cd_34": "889",
        "adm_cd_35": "656",
        "adm_cd_36": "468",
        "adm_cd_37": "777",
        "adm_cd_38": "901",
        "adm_cd_39": "122",
        "adm_cd_99": "32",
        "adm_cd_00_total": "884310",
        "adm_cd_11_total": "285665",
        "adm_cd_21_total": "36681",
        "adm_cd_22_total": "35177",
        "adm_cd_23_total": "54437",
        "adm_cd_24_total": "16126",
        "adm_cd_25_total": "17668",
        "adm_cd_26_total": "9591",
        "adm_cd_29_total": "3234",
        "adm_cd_31_total": "270695",
        "adm_cd_32_total": "16588",
        "adm_cd_33_total": "16154",
        "adm_cd_34_total": "26588",
        "adm_cd_35_total": "16182",
        "adm_cd_36_total": "11908",
        "adm_cd_37_total": "23170",
        "adm_cd_38_total": "30057",
        "adm_cd_39_total": "5630",
        "adm_cd_99_total": "8759"
    }
]
```

request
```
http://localhost:8000/covids?adm_cd_no=32&date=2022-08-21
```

response
```json
[
    {
        "date": "2022-08-21T00:00:00",
        "adm_cd_32": "3030",
        "adm_cd_32_total": "647421"
    }
]
```