#!python3
import requests
import appex
import ui
import os
import webbrowser
import dialogs
from math import ceil, floor

# NOTE: The ROWS variable determines the number of rows in "compact" mode. In expanded mode, the widget shows all shortcuts.
COLS = 3
ROWS = 3

# Each shortcut should be a dict with at least a 'title' and 'url' key. 'color' and 'icon' are optional. If set, 'icon' should be the name of a built-in image.
SHORTCUTS = [
    {'title': 'New Email', 'url': 'mailto:', 'color': '#5e96ff', 'icon': 'iow:email_24'},
    {'title': 'New Message', 'url': 'sms://', 'color': '#5ec0ff', 'icon': 'iow:chatbox_24'},
    {'title': 'Pythonista', 'url': 'pythonista3://', 'color': '#45d3e8', 'icon': 'iow:chevron_right_24'},
    {'title': 'Forum', 'url': 'http://forum.omz-software.com', 'color': '#4dd19d'},
    {'title': 'Google', 'url': 'http://google.com', 'color': '#a9de31'},
    {'title': 'DuckDuckGo', 'url': 'http://duckduckgo.com', 'color': '#ffd026'},
    {'title': 'Amazon', 'url': 'http://amazon.com', 'color': '#ff8e13'},
    {'title': 'Book', 'url': 'http://ebay.com', 'color': '#ff4a09'},
]

LIST_NUM = 3
API = 'https://api.douban.com/v2/book/search?q='


@ui.in_background
def get_books(sender):

    # 显示输入框，输入需要查询的内容
    key = dialogs.input_alert('输入要查询的内容','','取消','确定')
    #key = '心理学与生活'

    # 获取查询结果
    url = API + key
    response = requests.get(url)
    data = response.json()
    books = data['books']
    count = data['count']

    book_urls = []
    for i in range(min(LIST_NUM, count)):
        book_urls.append(books[i]['url'])

    # 结果显示
    '''v = ui.View(frame=(0, 0, 300, 110))
    button = ui.Button(title=sender.title, font=('<System>', 24), flex='rwh', action=get_books)
    button.frame = (0, 0, 150, 110)
    v.add_subview(button)
    appex.set_widget_view(v)'''


class LauncherView(ui.View):
    def __init__(self, shortcuts, *args, **kwargs):
        row_height = 110 / ROWS
        super().__init__(self, frame=(0, 0, 300, ceil(len(shortcuts) / COLS) * row_height), *args, **kwargs)
        self.buttons = []
        for s in shortcuts:
            btn = ui.Button(title=' ' + s['title'],
                            image=ui.Image(s.get('icon', 'iow:compass_24')),
                            name=s['url'],
                            action=self.button_action,
                            bg_color=s.get('color', '#55bcff'),
                            tint_color='#fff',
                            corner_radius=9)
            self.add_subview(btn)
            self.buttons.append(btn)

    def layout(self):
        bw = self.width / COLS
        bh = floor(self.height / ROWS) if self.height <= 130 else floor(110 / ROWS)
        for i, btn in enumerate(self.buttons):
            btn.frame = ui.Rect(i % COLS * bw, i // COLS * bh, bw, bh).inset(2, 2)
            btn.alpha = 1 if btn.frame.max_y < self.height else 0

    def button_action(self, sender):
        if str(sender.title) != ' Book':
            webbrowser.open(sender.name)
        else:
            get_books(sender)


def main():
    widget_name = __file__ + str(os.stat(__file__).st_mtime)
    v = appex.get_widget_view()

    # Optimization: Don't create a new view if the widget already shows the launcher.
    # 初始化 widget，如果已经存在则不显示
    if v is None or v.name != widget_name:
        v = LauncherView(SHORTCUTS)
        v.name = widget_name
        appex.set_widget_view(v)


if __name__ == '__main__':
    main()
