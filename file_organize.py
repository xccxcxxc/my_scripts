#! python3

import os
import shutil

path = '/Users/cx/Downloads/强制操作'
dirname = os.path.dirname(path)

os.chdir(dirname)
files = os.listdir(dirname)

for file in files:
    if os.path.isfile(file):
        if file.split('.')[0].isalnum():
            shutil.move(file, path)