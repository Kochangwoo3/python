import urllib.request

url = "https://uta.pw/shodou/img/28/214.png"  # 어떤 url에 있는 것을 가져올거니?
savename = "test214_urlopen.png"  # 어디에 저장할거니?

# 1. 다운로드
mem = urllib.request.urlopen(url).read()

# 2. 파일로 저장
with open(savename, mode="wb") as f: ## w:쓰기모드, b:바이너리모드
  f.write(mem)
  print("저장되었습니다..!")