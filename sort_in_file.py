# -*- coding: utf-8 -*-

# 对文件内的字符串排序, python sort_in_file.py [file]
import os

import sys


def sort_sfile(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = [line.lower() for line in lines]
        print(f'\nOriginal lines: {[(i, lines) for i, lines in enumerate(lines)]}')

    lines.sort()
    print(f'\nSorted lines: {[(i, lines) for i, lines in enumerate(lines)]}')
    ret = input('\nWould you want to write it to file? (y/n):')
    if ret.lower() == 'y':
        with open(file, 'w') as f:
            f.writelines(lines)


if __name__ == '__main__':
    file = sys.argv[1]
    sort_sfile(file)


