# -*- coding: utf-8 -*-
"""
遍历文件夹中的所有文件，根据扩展名进行过滤，在指定数组扩展名之外的文件进行显示
"""

import contextlib
import os
import queue
import requests
import sys
import threading
import time

FILTERS = [".jpg", ".gif", ".png", ".css"]
TARGET = "http://boodelyboo.com/wordpress"
THREADS = 10

answers = queue.Queue()
web_paths = queue.Queue()


def gather_paths():
    # os.walk 返回：1 当前文件夹名称 2 当前文件夹的子文件夹字符串列表 3 当前文件夹的文件字符串列表
    for root, _, files in os.walk('.'):
        for fname in files:
            if os.path.splitext(fname)[1] in FILTERS:
                continue
            path = os.path.join(root, fname)
            if path.startswith('.'):
                path = path[1:]
            print(path)
            web_paths.put(path)


@contextlib.contextmanager
def chdir(path):
    """
    On enter, change directory to specified path.
    On exit, change directory to original.
    """
    this_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(this_dir)


def test_remote():
    while not web_paths.empty():
        path = web_paths.get()
        url = f'{TARGET}{path}'
        time.sleep(2)
        r = requests.get(url)
        if r.status_code == 200:
            answers.put(url)
            sys.stdout.write('+')
        else:
            sys.stdout.write('x')

        sys.stdout.flush()


def run():
    mythreads = list()
    for i in range(THREADS):
        print(f'Spawning thread {i}')
        t = threading.Thread(target=test_remote())
        mythreads.append(t)
        t.start()

    for thread in mythreads:
        # 等待子线程结束，主线程才结束
        thread.join()


if __name__ == "__main__":
    """
    代码的执行顺序是：

    with语句首先执行chdir 函数中 yield之前的语句
    yield调用会执行with语句内部的所有语句
    最后执行yield之后的语句
    """
    with chdir("/home/kali/Downloads/wordpress"):
        gather_paths()
    input('Press return to continue.')
    run()
    with open('myanswer.txt', 'w') as f:
        while not answers.empty():
            f.write(f'{answers.get()}\n')
    print('done.')