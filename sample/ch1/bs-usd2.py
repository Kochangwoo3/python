from bs4 import BeautifulSoup
import urllib.request as req

# 1. html 가져오기
url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)
# 2. html 분석하기
soup = BeautifulSoup(res, "html.parser")

# 3. 추출하기
#exchangeList > li.on > a.head.usd > div > span.value
results = soup.select("div > span.value") # select 는 리스트리턴
#for result in results:
#  print(result.string)

#print("usd/krw =", price)

print("달러 = ", results[0].string)
print("엔화 = ", results[1].string)
print("유로 = ", results[2].string)

