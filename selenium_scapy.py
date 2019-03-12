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

url = 'https://18h.animezilla.com/manga/3405/55'
path = '/Users/cx/Downloads/银魂'
os.makedirs(path, exist_ok=True)

def nextUrl(soup):
    nextLinkElem = soup.select('a[rel="next"]')
    if len(nextLinkElem) == 0:
        return
    else:
        nextLink = nextLinkElem[0]
        nexturl = nextLink.get('href')
    return url

while True:
    # TODO: Download the page.
    # 必须先用 selenium 框架打开一次才能下载到清晰图，用 requests 无论如何伪装，得到都是缩略图
    driver.get(url)
    time.sleep(1)
    if "H" not in driver.title:
        driver.get(url)
        time.sleep(1)
        assert "H" in driver.title

    res = requests.get(url)
    if res.status_code != 200:
        continue

    soup = BeautifulSoup(res.text, 'html.parser')

    # TODO: Find the URL of the comic image.
    comicElem = soup.select('#comic')


    if len(comicElem) == 0:
        print('Could not find comic image.')
        break
    else:
        comicUrl = comicElem[0].get('src')

        # TODO: Download the image.
        print('Downloading image %s...' % comicUrl)

        driver.get(comicUrl)
        time.sleep(1)
        if str(os.path.basename(comicUrl)) not in driver.title:
            driver.get(comicUrl)
            assert str(os.path.basename(comicUrl)) in driver.title

        # TODO: Save the image to downloads.
        pyautogui.rightClick(720, 450)
        pyautogui.click(760, 475)
        time.sleep(1)
        pyautogui.typewrite(str(os.path.basename(url)))

        pyautogui.click(750, 305)

        # TODO: Get the next button's url.
        nextLinkElem = soup.select('a[rel="next"]')
        if len(nextLinkElem) == 0:
            break
        else:
            nextLink = nextLinkElem[0]
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