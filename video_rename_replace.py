# -*- coding: utf-8 -*-

# 通过替换字符串的方法给影视文件重新命名
import os

folder_path = input('Input folder path: ') or '/mnt/sda1/2TV/命运石之门'

# 切换到当前文件夹路径下
os.chdir(folder_path)
file_list = os.listdir(folder_path)
print(f'\nOld names: {file_list}')
old_head, new_head = input('Input old head and new head, use "," to split: ').split(',')
old_tail, new_tail = input('Input old tail and new tail, use "," to split: ').split(',')
new_names = []
for old_name in file_list:
    old_root, ext =  os.path.splitext(old_name)
    if ext != '':
        new_root = old_root.replace(old_head, new_head).replace(old_tail, new_tail)
        new_names.append(new_root+ext)
        os.rename(old_name, new_root+ext)

print('\nThe new names are: ')
print(new_names)
