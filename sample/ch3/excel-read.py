import openpyxl

# 엑셀 파일 열기
filename = "stats_104102.xlsx"
book = openpyxl.load_workbook(filename)

# 시트 추출
sheet = book.worksheets[0]

# 시트의 각 행을 순서대로 출력
data = []

for row in sheet.rows:
  data.append([
    row[0].value,
    str(row[10].value).replace(',','')
  ])

# 필요없는 줄 (헤더, 연도, 계) 제거
# del data[0]
# del data[1]
# del data[2]
for i in range(4): # [0,1,2,3]
  del data[0]

# 인구 순서로 정렬
data = sorted(data, key=lambda x:int(x[1]))

# for item in data:
#   print(item)

for i, item in enumerate(data):
  if (i >= 5): break
  print(i+1, item[0], int(item[1]))

