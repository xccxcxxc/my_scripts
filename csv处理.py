import csv
import re



oldFile = 'test.csv'


newTest = []
with open(oldFile, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if reader.line_num == 1:
            newTest.append(row)
            continue
        ipRex = re.compile(r'(\d{1,3}\.){1,3}\d{1,3}')
        ip = ipRex.search(row[-1])
        if ip is not None:
            row[-1] = ip.group()
            newTest.append(row)


with open('new'+oldFile, 'w', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    '''for row in newTest:
        print(row)
        writer.writerow(row)'''
    writer.writerows(newTest)