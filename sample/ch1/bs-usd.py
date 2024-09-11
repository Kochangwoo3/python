from bs4 import BeautifulSoup
import urllib.request as req

# 1. html 가져오기
url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)
# 2. html 분석하기
soup = BeautifulSoup(res, "html.parser")

# 3. 추출하기
#exchangeList > li.on > a.head.usd > div > span.value
price = soup.select_one("div > span.value").string
print("use/krw =", price)