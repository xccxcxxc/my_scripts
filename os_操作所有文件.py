"""
遍历当前目录中的所有文件，做相应操作
参考了 os_file_organize.py
"""
import os
import shutil

# os.getcwd 有可能是执行命令的目录而不是文件所在目录
base_dir = os.path.abspath(os.path.dirname(__file__))


def move_to_current_dir(foldername, file):
    # 如果目标文件已经存在，不覆盖
    if not os.path.exists(os.path.join(base_dir, file)):
        shutil.move(os.path.join(foldername, file), os.path.join(base_dir, file))
        print(os.path.join(foldername, file), os.path.join(base_dir, file))
    return


def copy_to_current_dir(foldername, file):
    # 如果目标文件已经存在，不覆盖
    if not os.path.exists(os.path.join(base_dir, file)):
        shutil.copy(os.path.join(foldername, file), os.path.join(base_dir, file))
        print(os.path.join(foldername, file), os.path.join(base_dir, file))
    return


def delete_file(foldername, file, ext=''):
    if os.path.splitext(file)[-1] == ext:
        print(os.path.join(foldername, file))
        os.remove(os.path.join(foldername, file))
    return


def do_something_to_file(foldername, file):
    # 调用具体代码
    # move_to_current_dir(foldername, file)
    # copy_to_current_dir(foldername, file)
    delete_file(foldername, file, ext='.pdf')
    return


# os.walk 返回：1 当前文件夹名称 2 当前文件夹的子文件夹字符串列表 3 当前文件夹的文件字符串列表
for foldername, subfolders, filenames in os.walk('.'):
    for file in filenames:
        do_something_to_file(foldername, file)


