#! python3
import requests
import os
from bs4 import BeautifulSoup

url = 'https://e-hentai.org/lofi/s/e5e3c75962/1356934-1'                # starting url
os.makedirs('eHentai', exist_ok=True)
while not url.endswith('#'):
    # TODO: Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')

    # TODO: Find the URL of the comic image.
    comicElem = soup.select('#sm')
    print("len = %s" % len(comicElem))
    if len(comicElem) == 0:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')

        # TODO: Download the image.
        print('Downloading image %s...' % comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()

        # TODO: Save the image to ./xkcd.
        imageFile = open(os.path.join('eHentai', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

        # TODO: Get the Prev button's url.
        prevLink = soup.select('div[id="ia"] a')[0]
        url = prevLink.get('href')

print('Done.')
