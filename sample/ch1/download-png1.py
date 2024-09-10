import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"  # 어떤 url에 있는 것을 가져올거니?
savename = "test214.png" # 어디에 저장할 거니?

urllib.request.urlretrieve(url, savename)
print("저장되었습니다...!")
