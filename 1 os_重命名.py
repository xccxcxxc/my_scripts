import os
folder_path = "/Volumes/Orico/001-100 国日双语 多国字幕"
file_list = os.listdir(folder_path)
# 切换到当前文件夹路径下
os.chdir(folder_path)
for old_name in file_list:
    if os.path.splitext(old_name)[-1] == 'mkv1':
        new_name = old_name[0:-1]
        os.rename(old_name, new_name)
        pass

# str.replace('ss', 's01') 可以进行字符串替换