# https://search.naver.com/search.naver
# ?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%B4%88%EC%BD%9C%EB%A6%BF

import sys
import urllib.request
import urllib.parse

# 명령줄 매개변수 추출
if len(sys.argv) <= 1:
  print("USAGE: download-forcast.py 107(Region Number)") 
  sys.exit()

regionNumber = sys.argv[1]

API = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
  'stnId' : regionNumber, 
}
params = urllib.parse.urlencode(values)

# 요청url생성
url = API + '?' + params
print("url=", url)
# 다운로드
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)