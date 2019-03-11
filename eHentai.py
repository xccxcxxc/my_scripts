#! python3
import pyautogui
import time
import requests
import os
import shutil
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)

url = 'https://e-hentai.org/lofi/s/10bbf7ff59/1372714-3'
path = '/Users/cx/Downloads/测试'
os.makedirs(path, exist_ok=True)

while True:
    # TODO: Download the page.
    # 必须先用 selenium 框架打开一次才能下载到清晰图，用 requests 无论如何伪装，得到都是缩略图
    driver.get(url)
    time.sleep(2.5)
    if "E-Hentai" not in driver.title:
        driver.get(url)
        assert "E-Hentai" in driver.title

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # TODO: Find the URL of the comic image.
    comicElem = soup.select('#sm')


    if len(comicElem) == 0:
        print('Could not find comic image.')
        break
    else:
        comicUrl = comicElem[0].get('src')

        # TODO: Download the image.
        print('Downloading image %s...' % comicUrl)

        driver.get(comicUrl)
        time.sleep(1.5)
        if str(os.path.basename(comicUrl)) not in driver.title:
            driver.get(comicUrl)
            assert str(os.path.basename(comicUrl)) in driver.title

        # TODO: Save the image to downloads.
        pyautogui.rightClick(720, 450, duration=0.25)
        pyautogui.click(760, 475, duration=0.25)
        time.sleep(0.5)
        pyautogui.typewrite(str(os.path.basename(url)))
        print(str(os.path.basename(url)))

        pyautogui.click(750, 305, duration=0.25)
        # TODO: Get the Prev button's url.
        nextLinkElem = soup.select('#ia a')
        if len(nextLinkElem) < 2:
            break
        else:
            nextLink = nextLinkElem[1]
            url = nextLink.get('href')

# 等待 2 秒文件全部保存完
time.sleep(2)
dirname = os.path.dirname(path)
os.chdir(dirname)
files = os.listdir(dirname)

for file in files:
    if os.path.isfile(file):
        if file.split('.')[0].isalnum():
            shutil.move(file, path)

print('Done.')