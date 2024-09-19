# https://nid.naver.com/nidlogin.login

from selenium.webdriver import Firefox, FirefoxOptions

USER = "userid"
PASS = "userpwd"

options = FirefoxOptions()
options.add_argument('-headless')

browser = Firefox(options=options)

# 로그인 페이지에 접근
url_login = " https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("로그인 페이지에 접근합니다.")

# 텍스트 박스에 아이디와 비밀번호 입력하기
# ID, NAME, XPATH, CSS_SELECTOR

e = browser.find_element("id", "id")
e.send_keys(USER)
e = browser.find_element("id", "pw")
e.send_keys(PASS)

browser.save_screenshot("Website_login.png")

browser.quit()

# 로그인 버튼 클릭

