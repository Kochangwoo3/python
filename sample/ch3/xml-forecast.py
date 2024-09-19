from bs4 import BeautifulSoup
import urllib.request as req
import os.path

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "forecast.xml"

if not os.path.exists(savename):
  req.urlretrieve(url, savename)

# BeautifulSoup로 분석
# request = req.urlopen(url)
# xml = request.read()
xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')
# seoul = soup.find_all("location")[0]

# 각 지역 확인
info = {}
for location in soup.find_all("location"):
  name = location.find("city").string
  weather = location.find("wf").string
  if not (weather in info):
    info[weather] = []
  info[weather].append(name)

# 각 지역의 날씨를 구분해서 출력하기
for weather in info.keys():
  print("+", weather)
  for city_name in info[weather]:
    print("| -", city_name)

# datas = seoul.find_all("data")
# for item in datas:
#   weather = item.find('wf').text
#   print(weather)