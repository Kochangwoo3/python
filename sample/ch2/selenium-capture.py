from selenium.webdriver import Firefox, FirefoxOptions

url = "http://www.naver.com/"

#Firefox 를 헤드리스 모드로
opts = FirefoxOptions()
opts.add_argument('-headless')

# PhantomJS 드라이버 추출
browser = Firefox(options=opts)

# url읽어들이기
browser.get(url)

# 화면을 캡쳐해서 저장하기
browser.save_screenshot("Website.png")

# 종료
browser.quit()