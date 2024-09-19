import codecs

# euc-kr로 저장된 csv 파일 읽기
filename = "test.csv"

csv = codecs.open(filename, "r", "euc_kr").read()

data = []
rows = csv.split("\r\n")

for row in rows:
  if row == "": continue
  cells = row.split(",")
  data.append(cells)

# 결과 출력
for c in data:
  print(c[1], c[2])