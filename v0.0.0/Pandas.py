import pandas as pd # Pandas 라이브러리를 사용하였습니다.
import requests # Requests 라이브러리를 사용하였습니다.

df = pd.DataFrame() # 데이터를 삽입할 비어있는 데이터프레임 객체를 생성하였습니다.

for page in range(1, 6): # 페이지 수를 의미하는 1부터 5까지의 숫자에 대해 반복하였습니다.

  url_005930 = "http://finance.naver.com/item/sise_day.nhn?code=005930" + "&page=" + str(page)
  # 네이버 금융의 삼성전자의 주식 정보가 있는 페이지에서 페이지 번호(&page=)를 str(page) 파라미터로 추가하였습니다.

  headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
  # 웹 서버가 웹 크롤링 요청을 웹 브라우저에서 온 것으로 인식하게 하기 위해 User-Agent 헤더 정보를 작성하였습니다.
  # 참고로 User-Agent 정보는 'https://useragentstring.com/'에서 획득할 수 있으며 이는 사용자의 웹 환경 등의 정보입니다.

  response = requests.get(url_005930, headers=headers)
  # 설정한 url에 HTTP GET 요청을 보낸 후 response 변수에 해당 응답을 저장하게 설정하였습니다.

  df = pd.concat([df, pd.read_html(response.text, header=0)[0]], ignore_index=True)
  # response에 저장된 HTML 내용 중 테이블을 pandas 데이터프레임으로 변환하였습니다.
  # 그리고 변환된 데이터프레임을 비어있는 기존 데이터프레임과 결합(concat)시켰습니다.
  # 새로운 데이터프레임의 인덱스값에 중복이 없도록 설정(ignore_index=True)하였습니다.

  # <참고 코드 : append 메소드>
  # df = df.append(pd.read_html(response.text, header=0)[0], ignore_index=True)
  # append 메소드는 concat과 비슷한 역할을 합니다.
  # append 메소드는 다른 데이터프레임을 행 방향(상-하)으로 결합시키는 기능을 수행합니다.
  # concat 메소드는 다른 데이터프레임을 행 방향 또는 열 방향(좌-우)으로 결합시킵니다.
  # 그러므로 데이터프레임을 더 유연하게 다루려면 concat 메소드를 사용하는 것이 더 바람직합니다.
  # 한편 Pandas 개발자들이 append 기능을 언젠가 라이브러리에서 제외시킬 예정이라고 합니다.

df = df.dropna() # 결측값이 있는 행을 삭제하였습니다.
df
# 데이터프레임을 출력하였습니다.
# 참고로 print(df)를 입력하면 데이터프레임이 출력되기는 하지만 시각화 정도가 좋지 않습니다.
# 단 두 글자뿐인 'df'를 입력하지 않으면 데이터프레임이 출력되지 않습니다.
