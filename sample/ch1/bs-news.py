from bs4 import BeautifulSoup
import urllib.request as req

# 1. html 가져오기
url = "http://news.naver.com/section/105"
res = req.urlopen(url)

# 2. html 분석
soup = BeautifulSoup(res, "html.parser")

# 3. 원하는 데이터 추출
results = soup.select("div.sa_text > a > strong")
for result in results:
  print(result.string)