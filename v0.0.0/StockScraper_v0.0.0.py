 # BeautifulSoup 활용의 장/단점
 # Naver Finance에서의 삼성전자(005930) stock information 추출 과정

from bs4 import BeautifulSoup
import requests

for page in range(1, 6):
  print(str(page))

  url_005930 = "http://finance.naver.com/item/sise_day.nhn?code=005930" + "&page=" + str(page)
  headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
  response = requests.get(url_005930, headers=headers)

  soup = BeautifulSoup(response.text, "html.parser")
  parsing_list = soup.find_all("tr")
  isCheckNone = None

  for i in range(1, len(parsing_list)):
    if(parsing_list[i].span != isCheckNone):
      print(parsing_list[i].find_all("td", align="center")[0].text,
            parsing_list[i].find_all("td", class_="num")[0].text)



# Pandas 활용의 장점
# 네이버 증권에서의 삼성증권(005930) stock information 추출 과정

import pandas as pd
import requests
df = pd.DataFrame()

for page in range(1, 6):
  url_005930 = "http://finance.naver.com/item/sise_day.nhn?code=005930" + "&page=" + str(page)
  headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
  response = requests.get(url_005930, headers=headers)
  df = df.append(pd.read_html(response.text, header=0)[0], ignore_index=True)

df = df.dropna()
df




# Pandas 활용의 단점
# Investing에서의 SCHD stock information 추출 과정

import pandas as pd
import requests
df = pd.DataFrame()

for page in range(1, 6):
  url_schd = "https://www.investing.com/etfs/schwab-us-dividend-equity-historical-data" + str(page)
  headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
  response = requests.get(url_schd, headers=headers)
  df = df.append(pd.read_html(response.text, header=0)[0], ignore_index=True)

df = df.dropna()
df
