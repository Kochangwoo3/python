# HTTP 통신
# HTTP 통신은 브라우저에서 서버로 요청(request)하고,
# 서버에서 브라우저로 응답(response)할 때
# 어떻게 할 것인지 나타내는 규약
# 특징 : 어떤 데이터를 가져가는지 등에 대한 정보(상태:STATE)를 저장하지 않는 통신
# 무상태(stateless) 통신
# http통신은 무상태 통신이지만
# 세션을 이용하면 쿠키에 기록되어 있는 고유ID를 키로 사용해
# 상태를 확인할 수 있음 - 상태유지(stateful)통신을 구현할 수 있음

# 로그인처리
# https://www.hanbit.co.kr/member/login_proc.php
# 방식 : POST


# urllib.request - 파이썬표준라이브러리, 구조약간복잡, http메서드 등을 직접 구현
# requests - 직관적이며 간단한 코드로 복잡한 요청처리가능

import requests
from bs4 import BeautifulSoup

# 세션만들기
session = requests.session()

# 로그인
# USER = "<본인아이디>"
# PASS = "<본인암호>"

USER = "hseumw2"
PASS = ""

url = "https://www.hanbit.co.kr/member/login_proc.php"
login_info = {
  "return_url" : "",
  "m_id": USER,
  "m_passwd": PASS
}
response = session.post(url, data=login_info)
response.raise_for_status()
print(response.text)



