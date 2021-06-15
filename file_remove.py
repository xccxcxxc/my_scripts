# -*- coding: utf-8 -*-

# 删除除包含指定词语之外的所有文件, python file_remove.py [path] [rsv]
import os
import sys


if __name__ == '__main__':
    path = sys.argv[1]
    rsv = sys.argv[2]
    delete_files = []
    reserved_files = []

    os.chdir(path)
    file_list = os.listdir(path)
    for file in file_list:
        if rsv in file:
            reserved_files.append(file)
        else:
            delete_files.append(file)

    print(f'\nThe reserved files are: ')
    reserved_files.sort()
    [print(file) for file in reserved_files]
    ret = input('\nDo you want to delete files? (y/n): ')
    if ret.lower() == 'y':
        [os.remove(file) for file in delete_files]

    sys.exit(0)

