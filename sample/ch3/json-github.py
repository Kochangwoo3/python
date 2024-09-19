import urllib.request as req
import json

json_str = req.urlopen("https://api.github.com/repositories").read()

# 문자열 => 파이썬 자료형
output = json.loads(json_str)
print(type(output))
#print(output)

for item in output:
  # 레포지토리명 - 소유주 정보에서 로그인 아이디
  print(item["name"] + " - " + item["owner"]["login"])