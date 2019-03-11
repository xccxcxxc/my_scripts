#! python3
import requests

LIST_NUM = 3
API = 'https://api.douban.com/v2/book/search?q='

key = '心理学与生活'
url = API + key
response = requests.get(url)
data = response.json()
books = data['books']
count = data['count']

book_urls = []

for i in range(min(LIST_NUM, count)):
    book_urls.append(books[i]['url'])

# print(book_urls)



