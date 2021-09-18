# -*- coding: utf-8 -*-
import time
import random
import requests

from lxml import etree



url = "https://e-hentai.org/lofi/s/6f3c258661/911274-1"
session = requests.session()
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
}
# 设置session的请求头信息
session.headers = headers
i = 1

while True:
    response = session.get(url)
    #print(response.content.decode())
    '''
    with open("test.png", 'w', encoding='utf8') as f:
        f.write(img.content.decode())   
    '''
    html = etree.HTML(response.content.decode())
    img_src = html.xpath("//img[@id='sm']/@src")[0]
    img = session.get(img_src)
    with open(str(i) + '.png', 'wb') as f:
        f.write(img.content)

    url = html.xpath("//a[text()='Next Page >']/@href")[0]
    #print(next_page)
    max_num = int(str(html.xpath("//a[text()='Next Page >']/../preceding-sibling::td/text()")[0]).split('/')[1])
    #print(max_num, type(max_num))
    if i == max_num:
        break
    i += 1
    print(i, max_num)
    time.sleep(random.randrange(0, 2000)/1000)

