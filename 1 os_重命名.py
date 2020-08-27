import os
folder_path = "/Users/linzehua/Desktop/Python代码练习/08/09"
file_list = os.listdir(folder_path)
# 切换到当前文件夹路径下
os.chdir(folder_path)
for old_name in file_list:
    new_name =  old_name[0:-1]
    os.rename(old_name, new_name)
    pass