#! python3

# 需要安装 PySocks 库
import requests


proxies = { "http": "socks5://127.0.0.1:1080", "https": "socks5://127.0.0.1:1080", }
print(requests.get('http://www.google.com', proxies=proxies).text)
'''url = 'https://e-hentai.org/lofi/s/570a203230/1125215-3'
url = 'http://www.google.com'
headers = {'user-agent': 'Googlebot-Image'}
proxies = { "http": "socks5://127.0.0.1:1080", "https": "socks5://127.0.0.1:1080", }
r = requests.get(url, proxies=proxies)
print(r.text)'''