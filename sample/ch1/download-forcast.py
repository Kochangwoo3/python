# https://search.naver.com/search.naver
# ?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=초콜릿

import urllib.request
import urllib.parse

API = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
  'stnId' : '108'
}
params = urllib.parse.urlencode(values)

# 요청 url 생성
url = API + "?" + params
print("url=", url)
# 다운로드
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)


