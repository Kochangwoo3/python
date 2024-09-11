# 신문기사 제목과 상세내용 링크
from bs4 import BeautifulSoup
import urllib.request as req
import time

# 1. html 가져오기
url = "http://news.naver.com/section/105"
res = req.urlopen(url)

# 2. html 분석
soup = BeautifulSoup(res, "html.parser")

# 3. 원하는 데이터 추출
results = soup.select("div.sa_text > a")
for result in results:
  print("제목: ", result.text.strip())
  # print("링크: ", result.attrs['href'])
  # 1. html 가져오기
  url_article = result.attrs['href']
  response = req.urlopen(url_article)
  # 2. html 분석
  soup_article = BeautifulSoup(response, "html.parser")
  # 3. 원하는 데이터 추출
  content = soup_article.select_one("#dic_area")
  print(content.contents)
  time.sleep(2)