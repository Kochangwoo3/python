import openpyxl
import openpyxl.styles

workbook = openpyxl.Workbook()

# 활성화된 시트 추출
sheet = workbook.active

sheet["A1"] = "테스트파일"
sheet["A2"] = "안녕하세요"
# 셀합침
sheet.merge_cells("A1:C1")
sheet["A1"].font = openpyxl.styles.Font(size=32, color="FF0000")

workbook.save("newFile.xlsx")

