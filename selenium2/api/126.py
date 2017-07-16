from selenium import webdriver
from time import *
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
siz = driver.find_element_by_id('cp').text
print(siz)
driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys('username')
driver.find_element_by_id('su').click()
driver.quit()