# 이미지 데이타 추출하기
import requests

r = requests.get("https://wikibook.co.kr/logo.png")

# 바이너리 형식으로 데이터 저장하기
with open("test.png", "wb") as f:
  f.write(r.content)
print("저장되었습니다.")