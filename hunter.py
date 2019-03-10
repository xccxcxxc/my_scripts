#! python3
import requests
import os
from bs4 import BeautifulSoup

url = 'https://18h.animezilla.com/manga/3403/4'  # starting url
'''headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}'''
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"}



basedir = '/Users/cx/女配角'
os.makedirs(basedir, exist_ok=True)

while True:
    # TODO: Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url, headers=headers)
    # res.raise_for_status()
    if res.status_code != 200:
        continue
    soup = BeautifulSoup(res.text, 'html.parser')

    # TODO: Find the URL of the comic image.
    comicElem = soup.select('#comic')
    print(type(comicElem))
    print("len = %s" % len(comicElem))
    if len(comicElem) == 0:
        print('Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')

        # TODO: Download the image.
        print('Downloading image %s...' % comicUrl)

        res = requests.get(comicUrl, headers=headers)
        if res.status_code != 200:
            continue
        # res.raise_for_status()

        # TODO: Save the image to ./xkcd.
        imageFile = open(os.path.join(basedir, str(os.path.basename(url)) + ".jpg"), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        '''title = os.path.join(basedir, str(os.path.basename(url)) + ".jpg")
        with open(title, 'wb') as file:
            file.write(res.content)'''

        # TODO: Get the Prev button's url.
        prevLinkElem = soup.select('a[rel="next"]')
        if len(prevLinkElem) == 0:
            break
        else:
            prevLink = prevLinkElem[0]
            url = prevLink.get('href')

print('Done.')
