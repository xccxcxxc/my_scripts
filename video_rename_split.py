# -*- coding: utf-8 -*-

# 通过对文件名分词的方法，给影视文件重新命名, python video_rename_split.py [path] [TV name]
import os
import re
import sys

if __name__ == '__main__':
    folder_path = sys.argv[1]
    tv_name = sys.argv[2]

    os.chdir(folder_path)
    file_list = os.listdir(folder_path)
    ret = re.split(r'\W+', file_list[0])
    print(f'\nThe file name is splited to:  {[(i, value) for i, value in enumerate(ret)]}')
    season, episode = input('\nPlease select the season and episode number: ').split()

    file_names = {}
    file_list.sort()
    for old_name in file_list:
        ret = re.split(r'\W+', old_name)
        if len(ret) > max(int(season), int(episode)):
            if season == episode:
                new_name = tv_name + '.' + ret[int(season)].upper() + '.' + ret[-1]
            else:
                new_name = tv_name + '.' + ret[int(season)].upper() + ret[int(episode)].upper() + '.' + ret[-1]
            file_names[old_name] = new_name

    print('\nThe new names are: ')
    [print(item) for item in file_names]

    ret = input('\nDo you really want to rename the files? (y/n): ')
    if ret.lower() == 'y':
        for key in file_names:
            if not os.path.exists(file_names[key]):
                os.rename(key, file_names[key])
    sys.exit(0)

