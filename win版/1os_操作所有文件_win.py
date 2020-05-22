"""
遍历当前目录中的所有文件，做相应操作
参考了 os_file_organize.py
"""
import os
import shutil
import csv


# os.getcwd 有可能是执行命令的目录而不是文件所在目录
#base_dir = os.path.abspath(os.path.dirname(__file__))
base_dir = "d:\\北京海关"
base_dir_compare = r"d:\北京海关"
#base_dir = "/Users/cx/Downloads/北京海关"
#oldFile = 'test.csv'

# 移动文件
def move_to_current_dir(foldername, file):
    # 如果目标文件已经存在，不覆盖
    if not os.path.exists(os.path.join(base_dir, file)):
        shutil.move(os.path.join(foldername, file), os.path.join(base_dir, file))
        print(os.path.join(foldername, file), os.path.join(base_dir, file))
    return

# 拷贝文件
def copy_to_current_dir(foldername, file):
    # 如果目标文件已经存在，不覆盖
    if not os.path.exists(os.path.join(base_dir, file)):
        shutil.copy(os.path.join(foldername, file), os.path.join(base_dir, file))
        print(os.path.join(foldername, file), os.path.join(base_dir, file))
    return

# 删除文件
def delete_file(foldername, file, ext=''):
    if os.path.splitext(file)[-1] == ext:
        print(os.path.join(foldername, file))
        os.remove(os.path.join(foldername, file))
    return


def do_something_to_file(foldername, file):
    # 调用具体代码
    # move_to_current_dir(foldername, file)
    # copy_to_current_dir(foldername, file)
    #delete_file(foldername, file, ext='.pdf')



    if os.path.splitext(file)[-1] == '.txt':
        absfile = os.path.join(foldername, file)
        with open(absfile, encoding='utf-8') as f:
            text = f.read()
        # 打印文件名
        print(absfile)
        list_txt = text.split()

        i = 0
        for info in list_txt:
            print(f'info{i}:{info}')
            i += 1

        # 以下为高度模板定制化内容，都是死的
        name = ""
        if "1．姓名：" in list_txt:
            index = list_txt.index("1．姓名：")
            name = list_txt[index+1]

        sex = ""
        if "性别：" in list_txt:
            index = list_txt.index("性别：")
            sex = list_txt[index+1]

        birth = ""
        if "出生年月：" in list_txt:
            index = list_txt.index("出生年月：")
            birth = list_txt[index + 1]

        hometown = ""
        if "籍贯：" in list_txt:
            index = list_txt.index("籍贯：")
            hometown = list_txt[index+1]

        id = ""
        if "身份证号：" in list_txt:
            index = list_txt.index("身份证号：")
            id = 'ID:' + list_txt[index + 1]

        height = ""
        if "2．身高：" in list_txt:
            index = list_txt.index("2．身高：")
            height = list_txt[index + 1]

        weight = ""
        if "体重：" in list_txt:
            index = list_txt.index("体重：")
            weight = list_txt[index + 1]

        blood = ""
        if "血型：" in list_txt:
            index = list_txt.index("血型：")
            blood = list_txt[index + 1]

        department = ""
        bj_id = ""
        if "关员号：" in list_txt:
            bj_id_index = list_txt.index("关员号：")
            bj_id = list_txt[bj_id_index + 1]
            if "3．所在单位及职务职级：" in list_txt:
                index = list_txt.index("3．所在单位及职务职级：")
                department = list_txt[index + 1]
                index+=1
                while index<bj_id_index-1:
                    department = department + " " + list_txt[index+1]
                    index += 1

        disease_history = []
        if "4." in list_txt:
            index = list_txt.index("4.")
            disease_history += list_txt[(index+1):(index+5)]

        healthy = ''
        if "2020年以来，是否出现过发热、乏力、咳嗽、腹泻等以下不适症状？" in list_txt:
            index = list_txt.index("2020年以来，是否出现过发热、乏力、咳嗽、腹泻等以下不适症状？")
            healthy = list_txt[(index+1)]

        flu = ''
        if "疫情期间流行病学史（对2020年以来本人离返京情况、参与聚餐聚会情况、进行过哪些活动以及春节期间本人去向等动态情况描述）：" in list_txt:
            index = list_txt.index("疫情期间流行病学史（对2020年以来本人离返京情况、参与聚餐聚会情况、进行过哪些活动以及春节期间本人去向等动态情况描述）：")
            flu = list_txt[(index + 1)]

        first_date = ''
        first_moon = ''
        first_sun = ''
        if "第1次" in list_txt:
            index = list_txt.index("第1次")
            if '□阴性' not in list_txt[index+1]:
                first_date = list_txt[index+1]
                first_moon = list_txt[index+2]
                first_sun = list_txt[index+3]
            else:
                first_moon = list_txt[index + 1]
                first_sun = list_txt[index + 2]

        parent_fold = foldername
        while os.path.dirname(parent_fold) != base_dir_compare:
            print(f"----------------{os.path.dirname(parent_fold)}------{base_dir_compare}------")
            parent_fold = os.path.dirname(parent_fold)

        '''if os.path.dirname(parent_fold) != base_dir_compare:
            print("----------------wht")

        print(f"----------------{os.path.dirname(parent_fold)}------{base_dir_compare}------")'''
        fold = os.path.basename(parent_fold)

        print(f'目录：{fold} 姓名:{name} 性别:{sex} 出生年月：{birth} 籍贯:{hometown} 身份证号：{id} ')
        print(f'身高：{height} 体重：{weight} 血型：{blood} 所在单位及职务职级：{department} 关员号：{bj_id}')
        print(f'{disease_history[0]} {disease_history[1]} {disease_history[2]} {disease_history[3]}')
        print(f'健康状况:{healthy} 流行病学调查:{flu}')
        print(f'第1次日期：{first_date} 第1次阴性结果：{first_moon} 第1次阳性结果：{first_sun}')

        row = [fold, name, sex, birth, hometown, id, height, weight, blood, department, bj_id, disease_history[0],\
               disease_history[1],disease_history[2],disease_history[3], healthy, flu, first_date, first_moon, first_sun]
        with open('D:\\Downloads\\output.csv', 'a', encoding='utf-8-sig') as csv_f:
            writer = csv.writer(csv_f)
            writer.writerow(row)

    return


# os.walk 返回：1 当前文件夹名称 2 当前文件夹的子文件夹字符串列表 3 当前文件夹的文件字符串列表
for foldername, subfolders, filenames in os.walk(base_dir):
    for file in filenames:
        do_something_to_file(foldername, file)


