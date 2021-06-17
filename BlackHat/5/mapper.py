# -*- coding: utf-8 -*-

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


if __name__ == "__main__":
    with chdir("/home/kali/Downloads/wordpress"):
        gather_paths()
    input('Press return to continue.')