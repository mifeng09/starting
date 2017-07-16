import xlrd

wbk = xlrd.open_workbook('test.xls')
sheet_names = wbk.sheet_names()
# for sheet_name in sheet_names:
sheet1 = wbk.sheet_by_index(0)
print(sheet1.row_values(1))
