import csv, codecs
# codecs 파이썬에서 다양한 문자 인코딩과 디코딩을 위한 도구를
#        제공하는 표준 라이브러리 모듈입니다.

with codecs.open("test.csv", "w", "euc_kr") as fp:
  writer = csv.writer(fp, delimiter=",", quotechar='"')
  writer.writerow(["ID", "이름", "가격"])
  writer.writerow(["1000", "SD 카드", 30000])
  writer.writerow(["1001", "키보드", 21000])
  writer.writerow(["1002", "마우스", 15000])