#! python3
import requests
#import os
#import webbrowser
#import dialogs
from bs4 import BeautifulSoup


class Website:
    def __init__(self, name, url, searchUrl, resultListing,
                 resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Crawler:
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text()
        return ''

    def search(self, topic, site):
        bs = self.getPage(site.searchUrl + topic)
        results = bs.select(site.resultListing)
        url = results[0].select(site.resultUrl)[0].attrs['href']
        #webbrowser.get('safari').open(url)

def main():
    # 显示输入框，输入需要查询的内容
    #key = dialogs.input_alert('输入要查询的内容', '', '', '确定')
    key = '呼啸山庄'
    siteData = [['豆瓣', 'https://book.douban.com', 'https://book.douban.com/subject_search?search_text=',
                 'div.item-root', 'div.title a', True, 'title', 'section#product-description']]
    sites = []
    for row in siteData:
        sites.append(Website(row[0], row[1], row[2], row[3],
                             row[4], row[5], row[6], row[7]))
    site = sites[0]
    crawler = Crawler()
    crawler.search(key, site)


if __name__ == '__main__':
    main()

