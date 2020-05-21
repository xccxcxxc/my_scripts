"""
遍历当前目录中的所有文件，做相应操作
参考了 os_file_organize.py
"""
import os
import shutil
import re

# os.getcwd 有可能是执行命令的目录而不是文件所在目录
#base_dir = os.path.abspath(os.path.dirname(__file__))
base_dir = "d:\\20机关党委"

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

    # 打印特定后缀的文件
    if os.path.splitext(file)[-1] == '.txt':
        print(f'fold:{foldername}, file:{file}, name:{os.path.splitext(file)[0]}')

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
        index = list_txt.index("1．姓名：")
        name = list_txt[index+1]
        sex = ""
        if "性别：" in list_txt:
            index = list_txt.index("性别：")
            sex = list_txt[index+1]
        print(f'name:{name} sex:{sex}')

    return


# os.walk 返回：1 当前文件夹名称 2 当前文件夹的子文件夹字符串列表 3 当前文件夹的文件字符串列表
for foldername, subfolders, filenames in os.walk(base_dir):
    for file in filenames:
        do_something_to_file(foldername, file)


