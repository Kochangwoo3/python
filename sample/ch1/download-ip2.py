# url확인 접근해서 결과 출력하기
# 모듈 읽어들이기
import urllib.request

# import requests
# response = requests.get("https://www.google.co.kr")

# 데이터 읽어들이기
url = "https://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()
# print(mem)
# 바이너리를 문자열로 변환하기
text = data.decode("utf-8")
print(text)

