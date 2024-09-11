from bs4 import BeautifulSoup
import re

html = """
<ul>
  <li><a href="hoge.html">hoge</li>
  <li><a href="https://example.com/fuga">fuga*</li>
  <li><a href="https://example.com/foo">foo*</li>
  <li><a href="http://example.com/aaa">aaa</li>
</ul>
"""

soup = BeautifulSoup(html, "html.parser")
# 정규 표현식으로 href 속성에서 https인 것 추출하기
li = soup.find_all(href=re.compile(r"^https://"))
for e in li:
  print(e.attrs['href'])