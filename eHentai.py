# -*- coding: utf-8 -*-
import time
import random
import os
import pathlib
import shutil
import zipfile
import requests

from lxml import etree

url = 'https://e-hentai.org/lofi/s/42b847d9c8/1829683-1'
#url = 'https://e-hentai.org/lofi/s/2faeb29c17/1644336-1'
dir_name = 'test'
zip_name = 'test.zip'
session = requests.session()
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
}
# 设置session的请求头信息
session.headers = headers


# zipfilename 是压缩包名字，dirname 是要打包的目录
def compress_file(zipfilename, dirname):
    if os.path.isfile(dirname):
        with zipfile.ZipFile(zipfilename, 'w') as z:
            z.write(dirname)
    else:
        with zipfile.ZipFile(zipfilename, 'w') as z:
            for root, dirs, files in os.walk(dirname):
                for single_file in files:
                    if single_file != zipfilename:
                        filepath = os.path.join(root, single_file)
                        z.write(filepath)


if not pathlib.Path(dir_name).exists():
    os.mkdir(dir_name)
i = 1
response = session.get(url)
html = etree.HTML(response.content.decode())
max_num = int(str(html.xpath("//a[text()='Next Page >']/../preceding-sibling::td/text()")[0]).split('/')[1])
while True:
    response = session.get(url, timeout=5)
    #print(response.content.decode())

    html = etree.HTML(response.content.decode())
    img_src = html.xpath("//img[@id='sm']/@src")[0]
    img = session.get(img_src, timeout=(5, 30))
    with open(dir_name + '/' + str(i) + '.png', 'wb') as f:
        f.write(img.content)

    if i == max_num:
        compress_file(zip_name, dir_name)
        shutil.rmtree(dir_name)
        break
    i += 1
    url = html.xpath("//a[text()='Next Page >']/@href")[0]
    print(i, max_num)
    #time.sleep(random.randrange(0, 500)/1000)
