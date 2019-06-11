import openpyxl
import re
import os


excelFile = 'test.xlsx'
sheetName = 'test'

for excelFile in os.listdir('.'):
    if os.path.splitext(excelFile)[-1] == '.xlsx':
        wb = openpyxl.load_workbook(excelFile)
        #sheetnames = wb.get_sheet_names()
        sheet = wb[wb.sheetnames[0]]

        for rowNum in range(2, sheet.max_row):
            # print(sheet['F' + str(rowNum)].value)
            ipRex = re.compile(r'(\d{1,3}\.){1,3}\d{1,3}')
            ip = ipRex.search(sheet['F'+str(rowNum)].value)
            # print(ip.group())
            sheet.cell(row=rowNum, column=7).value = ip.group()

        wb.save(excelFile)