# https://search.naver.com/search.naver
# ?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%B4%88%EC%BD%9C%EB%A6%BF

import urllib.request
import urllib.parse

API = "https://search.naver.com/search.naver"
values = {
  'where' : 'nexearch', 
  'sm' : 'top_hty',
  'fbm' : '0',
  'ie' : 'utf8',
  'query' : '초콜릿'
}
params = urllib.parse.urlencode(values)

# 요청url생성
url = API + '?' + params
print("url=", url)
# 다운로드
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)