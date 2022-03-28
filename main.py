#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/home/guerdon/.config/google-chrome/System\ Profile/")
options.add_argument('--profile-directory="Profile 1"')
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://app.tophat.com/e/648330/lecture/')

l = driver.find_element_by_tag_name("input")
while true:
    l.send_keys(webdriver.common.keys.Keys.TAB)
    l.send_keys(webdriver.common.keys.Keys.ENTER)
