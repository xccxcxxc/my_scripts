#! python3
import requests
import os
import webbrowser
import dialogs

LIST_NUM = 3
API = 'https://api.mobile.com/v2/book/search?q='
URL = 'https://book.mobile.com/subject/'


def main():
    # 显示输入框，输入需要查询的内容
    key = dialogs.input_alert('输入要查询的内容', '', '', '确定')

    # 获取查询结果
    url = API + key
    response = requests.get(url)
    data = response.json()
    books = data['books']
    count = data['count']

    book_urls = []
    for i in range(min(LIST_NUM, count)):
        book_url = URL + str(os.path.basename(books[i]['url']))
        book_urls.append(book_url)

    # 结果显示
    webbrowser.get('safari').open(book_urls[0])


if __name__ == '__main__':
    main()

