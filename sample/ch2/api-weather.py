import requests
import json

apikey = "100032b2f73bdecaa72398d3ac2d3f28"

cities = ["Seoul,KR", "Tokyo,JP", "New York,US"]

api = "https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

for name in cities:
  url = api.format(city=name, key=apikey)
  r = requests.get(url)

  # 결과를 json형식으로 변환
  data = json.loads(r.text)
  print("+ 도시 =", data["name"])
  print("| 날씨 =", data["weather"][0]["description"])