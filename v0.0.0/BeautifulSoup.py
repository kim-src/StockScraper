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
