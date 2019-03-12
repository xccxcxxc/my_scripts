#! python3
import requests
import webbrowser
import dialogs

LIST_NUM = 3
API = 'https://api.mobile.com/v2/movie/search?q='
URL = 'https://movie.mobile.com/subject/'


def main():
    # 显示输入框，输入需要查询的内容
    key = dialogs.input_alert('输入要查询的内容', '', '', '确定')

    # 获取查询结果
    url = API + key
    response = requests.get(url)
    data = response.json()
    movie_url = URL + data['subjects'][0]['id']

    # 结果显示
    webbrowser.get('safari').open(movie_url)


if __name__ == '__main__':
    main()

