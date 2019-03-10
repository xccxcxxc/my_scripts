#! python3

import time
import pyautogui
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)

url = 'https://18h.animezilla.com/manga/3403/4'  # starting url
driver.get(url)
assert "H" in driver.title
url = 'https://m.iprox.xyz/s/20180709/09923b65.png'
driver.get(url)
assert "9" in driver.title
pyautogui.rightClick(720,450)
pyautogui.click(760, 475)
time.sleep(2)
pyautogui.typewrite('1')

pyautogui.click(750, 305)

#pyautogui.moveTo(760, 305)