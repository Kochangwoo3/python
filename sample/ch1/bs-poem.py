from bs4 import BeautifulSoup
import urllib.request as req

# 1. html 가져오기
url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)

# 2. html 분석
soup = BeautifulSoup(res, "html.parser")

# 3. 데이터 추출
# #mw-content-text
a_list = soup.select("#mw-content-text ul > li > a")
for a in a_list:
  name = a.string
  print("-", name)