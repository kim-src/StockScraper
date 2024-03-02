### 🎁 Tunnel
- [StockScraper 세부내용 (글제목 : 웹 크롤링을 이용한 데이터 분석)](https://kim-src.github.io/categories/toy-project/)
- [링크드인 프로필 (Chang-Seong Kim)](https://www.linkedin.com/in/chang-seong-kim-7826142a0/)

<br>

# ✅ Stock Price Information

<br>

### 🔔 주식 종가 조회 시스템
> - 주요 언어 : Python  
> - 주요 라이브러리 : BeautifulSoup, Pandas  
> - 조회 사이트 : 네이버 증권, investing  
> - 주식 종목 : 삼성전자(005930), SCHD ETF  
> - 조회 내용 : 200일 동안의 삼성전자 일별 종가, SCHD ETF의 최근 종가  

<br>

### 📌 조회 방법 : BeautifulSoup
> - 삼성전자 종목 페이지에서 종가가 기입된 페이지를 for 반복문으로 조회  
> - 페이지 당 기입된 10개 행에 대해 해당 거래일 및 종가를 for 반복문으로 조회  
> - 조회된 내용을 text 형식으로 return  

<br>

### 📌 코드 요약 : BeautifulSoup
> - bs4 : BeautifulSoup library ver. 4  
> - requests : url, header 정보를 이용하여 웹 페이지의 HTML 문서 요청  
> - response : 요청한 HTML 문서 회신  
> - URL Information : finance.naver.com
> - Header Information : useragentstring.com  
> - parser : 문서의 내용을 토큰으로 구분하고 파스트리 생성
> - isCheckNone : None 값 필터링하여 제외

<br>

### 📌 조회 방법 : Pandas
> - 삼성전자 종목 페이지에서 종가가 기입된 페이지를 DataFrame 모듈로 조회
> - 조회한 페이지에서 read_html 모듈로 거래일, 종가 등의 데이터 추출
> - 추출된 내용을 text 형식으로 return

<br>

### 📌 코드 요약 : Pandas
> - DataFrame : Pandas Module
> - append : Pandas Module
> - read_html : Pandas Module
> - ignore_index = True : Pandas Module
> - dropna : Pandas Module

<br>

### 🎁 References
> - FastCampus의 Selena 강사님 강의

***

<br>
<br>
<br>
