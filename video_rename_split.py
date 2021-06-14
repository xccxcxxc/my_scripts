# -*- coding: utf-8 -*-

# 通过对文件名分词的方法，给影视文件重新命名
import os
import re

folder_path = input('Input folder path: ') or '/mnt/sda1/2TV/命运石之门'

# 切换到当前文件夹路径下
os.chdir(folder_path)
file_list = os.listdir(folder_path)
ret = re.split(r'\W+', file_list[0])
print(f'\nPlease select the season and episode number:  {[(i, value) for i, value in enumerate(ret)]}')
season, episode = input('\nInput: ').split()

new_names = []
for old_name in file_list:
    ret = re.split(r'\W', old_name)
    if len(ret) > int(episode):
        if season == episode:
            new_name = ret[int(season)] + '.' + ret[-1]
        else:
            new_name = ret[int(season)] + ret[int(episode)] + '.' + ret[-1]
        new_names.append(new_name)
        # TODO: 判断下是否有重复命名，否则会抛出异常
        os.rename(old_name, new_name)
print('\nThe new names are: ')
print(new_names)
