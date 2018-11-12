# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Firefox()
site_url = "http://blog.csssr.ru/qa-engineer/"
driver.get(site_url)

find_tab = driver.find_element_by_link_text("НАХОДИТЬ НЕСОВЕРШЕНСТВА")
find_tab.click()
time.sleep(1)
soft_link = driver.find_element_by_link_text("Софт для быстрого создания скриншотов")
link = soft_link.get_attribute("href")
print("The link on the page: " + link)
assert link == 'https://monosnap.com/'
print("The link was correct")
