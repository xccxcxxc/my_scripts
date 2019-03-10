#! python3
import pyautogui
import time
import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)

url = 'https://18h.animezilla.com/manga/3403/69'  # starting url
basedir = '/Users/cx/Downloads/女配角'
os.makedirs(basedir, exist_ok=True)

while True:
    # TODO: Download the page.
    # 必须先用 selenium 框架打开一次才能下载到清晰图，用 requests 无论如何伪装，得到都是缩略图
    driver.get(url)
    assert "H" in driver.title

    res = requests.get(url)
    if res.status_code != 200:
        continue

    soup = BeautifulSoup(res.text, 'html.parser')

    # TODO: Find the URL of the comic image.
    comicElem = soup.select('#comic')


    if len(comicElem) == 0:
        print('Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')

        # TODO: Download the image.
        print('Downloading image %s...' % comicUrl)

        driver.get(comicUrl)
        assert str(os.path.basename(comicUrl)) in driver.title

        # TODO: Save the image to downloads.
        pyautogui.rightClick(720, 450)
        pyautogui.click(760, 475)
        time.sleep(2)
        pyautogui.typewrite(str(os.path.basename(url)))

        pyautogui.click(750, 305)

        # TODO: Get the Prev button's url.
        prevLinkElem = soup.select('a[rel="next"]')
        if len(prevLinkElem) == 0:
            break
        else:
            prevLink = prevLinkElem[0]
            url = prevLink.get('href')

print('Done.')
