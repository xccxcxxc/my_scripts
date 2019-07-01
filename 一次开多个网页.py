#! python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

start_page = 460
page_num = 20
url = 'http://hotbaidu.com/category/uncategorized/page/'


options = Options()
options.binary_location = "./chrome/chrome.exe"
driver = webdriver.Chrome(executable_path="./chrome/chromedriver.exe", options=options)
driver.get(f'{url}{start_page}')
driver.maximize_window()
#driver.set_window_size(1366,768)
first_handle = driver.current_window_handle


for i in range(start_page+1, start_page+page_num):
    new_window = f'window.open("{url}{i}")'
    driver.execute_script(new_window)

driver.switch_to.window(first_handle)