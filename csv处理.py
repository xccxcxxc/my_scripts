import csv
import re


oldFile = 'test.csv'
newFile = 'newTest.csv'

newTest = []
with open(oldFile, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        ipRex = re.compile(r'(\d{1,3}\.){1,3}\d{1,3}')
        ip = ipRex.search(row[-1])
        if ip is not None:
            row[-1] = ip.group()
        newTest.append(row)


with open(newFile, 'w', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    '''for row in newTest:
        print(row)
        writer.writerow(row)'''
    writer.writerows(newTest)