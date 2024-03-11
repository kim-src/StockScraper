### 🎁 Tunnel
- [StockScraper 세부내용 (글제목 : 웹 크롤링을 이용한 데이터 분석)](https://kim-src.github.io/categories/toy-project/)
- [Kim의 개발 프로젝트 모음 (깃허프 레포지토리)](https://github.com/Kim-src/All-Projects)
- [링크드인 프로필 (Chang-Seong Kim)](https://www.linkedin.com/in/chang-seong-kim-7826142a0/)

<br>

## ✅ StockScraper 소개
> - 개발 환경 : Google Colab
> - 개발 목적 : Python을 이용한 웹 크롤링 경험 및 Colab 활용 겸험 습득
> - 개발 내용 : 네이버 증권 사이트를 이용한 삼성전자 주식 정보 수집
> - 개발 역량 : Colab 활용, Python의 BeautifulSoup, Pandas, Requests 활용, 웹 크롤링 이해
> - 상세 내용 : <a href="https://kim-src.github.io/categories/toy-project/">웹 크롤링을 이용한 데이터 분석 (블로그 카테고리)</a>
> - 개발에 필요했던 기능 :  
> <img alt="Google Colab" src="https://img.shields.io/badge/-Google_Colab-F9AB00?style=flat-square&logo=google-colab&logoColor=white" /> <img alt="Python" src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" /> <img alt="BeautifulSoup" src="https://img.shields.io/badge/BeautifulSoup-2ca02c.svg?style=flat-square&logo=python&logoColor=white" /> <img alt="Pandas" src="https://img.shields.io/badge/Pandas-white.svg?style=flat-square&logo=pandas&logoColor=black" /> <img alt="Requests" src="https://img.shields.io/badge/Requests-2CA5E0.svg?style=flat-square&logo=python&logoColor=white" />
> 
> #### 🎯 학습 결론
> - 웹 크롤링 기능을 구현할 수 있는 간단한 프로그램을 제작하였습니다.
> - 웹 크롤링을 이용하여 HTML로 구성된 웹 페이지 정보를 쉽게 가져올 수 있었습니다.
> - 더 나아가면 검색 엔진 프로그램 개발에 활용될 수 있을 것 같습니다.
> - 그런데 웹 크롤링은 수많은 데이터 분석 방법 중 단지 하나의 도구일뿐이었습니다.
> - 물론 자동화 프로그램 개발도 중요하지만 데이터 수집 계획 및 해석 방법이 더 중요한 것 같습니다.

<br>

## 🔔 배경 지식
### 📌 웹 크롤링(Web Crawling)
> - 데이터 분석 또는 검색 엔진 구축의 한 방법으로 웹 페이지에 있는 데이터를 추출하는 것입니다.
> - Pyhton의 반복문 및 Requests 라이브러리를 이용하면 웹 크롤링 기능을 구현할 수 있습니다.
> - 블로그 글에서는 웹 크롤링 기능을 이용한 주식 정보 데이터 분석 방법을 작성하였습니다.

### 📌 BeautifulSoup
> - BeautifulSoup는 대표적인 웹 크롤링 목적의 Python 라이브러리입니다.
> - BeautifulSoup는 HTML 또는 XML 등의 언어에서 데이터를 추출하는 기능을 제공합니다.

### 📌 Pandas
> - Pandas는 데이터 가공 목적의 Python 라이브러리입니다.
> - 데이터 분석 시 데이터를 DB 형식으로 빠르게 변환시킬 수 있습니다.
> - 또는 다양한 데이터와 조합시키거나 데이터 필터링 시 이용됩니다.
> - 그래서 BeautifulSoup로 데이터를 취득한 후 Pandas로 변환하는 작업을 하기도 합니다.

<br>

***

<br>
<br>
<br>



``` python
from bs4 import BeautifulSoup # BeautifulSoup 라이브러리를 사용하였습니다.
import requests # Requests 라이브러리를 사용하였습니다.

for page in range(1, 6): # 페이지 수를 의미하는 1부터 5까지의 숫자에 대해 반복하였습니다.

  print(str(page))
  # 현재 페이지 번호를 출력하도록 설정하였습니다.
  
  url_005930 = "http://finance.naver.com/item/sise_day.nhn?code=005930" + "&page=" + str(page)
  # 네이버 금융의 삼성전자의 주식 정보가 있는 페이지에서 페이지 번호(&page=)를 str(page) 파라미터로 추가하였습니다.

  headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
  # 웹 서버가 웹 크롤링 요청을 웹 브라우저에서 온 것으로 인식하게 하기 위해 User-Agent 헤더 정보를 작성하였습니다.
  # 참고로 User-Agent 정보는 'https://useragentstring.com/'에서 획득할 수 있으며 이는 사용자의 웹 환경 등의 정보입니다.

  response = requests.get(url_005930, headers=headers)
  # 설정한 url에 HTTP GET 요청을 보낸 후 response 변수에 해당 응답을 저장하게 설정하였습니다.

  soup = BeautifulSoup(response.text, "html.parser")
  # response에 저장된 응답 중 HTML 내용을 사용하여 BeautifulSoup 객체를 생성하였습니다.
  # BeautifulSoup 객체를 이용하여 HTML 내용을 파싱(분석)할 수 있습니다.

  parsing_list = soup.find_all("tr")
  # HTML 내용 중 'tr' 태그가 포함된 모든 문자열(행)을 찾아 리스트로 반환시켰습니다.

  isCheckNone = None
  # None 값에 대한 비교를 위한 변수를 설정하였습니다.
  
  for i in range(1, len(parsing_list)):
  # parsing_list 내용에 있는 'tr' 태그가 포함된 행을 반복하였습니다.

    if(parsing_list[i].span != isCheckNone):
    # 유효한 데이터 행 정보만 취득하기 위해 'span' 태그의 내용이 None이 아닌지 확인하였습니다.

      print(parsing_list[i].find_all("td", align="center")[0].text,
            # 해당 'tr' 태그 내에서 'td' 태그 중 align 속성이 "center"인 첫 번째 요소([0])의 텍스트(날짜)를 출력합니다.

            parsing_list[i].find_all("td", class_="num")[0].text)
            # 같은 'tr' 태그 내에서 'td' 태그 중 class 속성이 "num"인 첫 번째 요소([0])의 텍스트(주식 종가)를 출력합니다.
```
