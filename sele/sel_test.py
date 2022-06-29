import os


import os
os.system(r'echo me > test.txt')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(r'C:\Users\timothee\Desktop\Nuovacartella\chromedriver.exe', options=chrome_options)
print('HI')
driver.get('https://rts.ch')
driver.save_screenshot(r"C:\Users\timothee\Desktop\screenshot.png")
driver.close()
print('me')