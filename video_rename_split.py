# -*- coding: utf-8 -*-

# 通过对文件名分词的方法，给影视文件重新命名, python video_rename_split.py [path] [TV name]
# [path]为 BASE_PATH 下的相对路径
import os
import re
import sys

BASE_PATH = '/mnt/sda1/2TV/'

if __name__ == '__main__':
    # folder = input(f'\n\nInput the folder, base path is "{BASE_PATH}": ')
    folder = sys.argv[1]
    tv_name = sys.argv[2]
    folder_path = BASE_PATH + folder

    os.chdir(folder_path)
    file_list = os.listdir(folder_path)
    ret = re.split(r'\W+', file_list[0])
    print(f'\nThe file name is splited to:  {[(i, value) for i, value in enumerate(ret)]}')
    season, episode = input('\nPlease select the season and episode number: ').split()

    new_names = []
    for old_name in file_list:
        ret = re.split(r'\W', old_name)
        if len(ret) > int(episode):
            if season == episode:
                new_name = tv_name + '-' + ret[int(season)].upper() + '.' + ret[-1]
            else:
                new_name = tv_name + '-' + ret[int(season)].upper() + ret[int(episode)].upper() + '.' + ret[-1]
            new_names.append(new_name)
            if not os.path.exists(new_name):
                os.replace(old_name, new_name)
    print('\nThe new names are: ')
    print(new_names)

