from openpyxl import load_workbook
from re import compile


excelFile = 'test.xlsx'
sheetName = 'test'

wb = load_workbook(excelFile)
sheet = wb[sheetName]


for rowNum in range(2, sheet.max_row):
    #print(sheet['F' + str(rowNum)].value)
    ipRex = compile(r'(\d{1,3}\.){1,3}\d{1,3}')
    ip = ipRex.search(sheet['F'+str(rowNum)].value)
    #print(ip.group())
    sheet.cell(row=rowNum, column=7).value = ip.group()

wb.save(excelFile)