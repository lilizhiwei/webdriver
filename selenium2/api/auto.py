from selenium import webdriver
import os
from time import sleep
driver = webdriver.Firefox()

driver.get('https://www.yyddd.com/pc/login.html')
sleep(5)
driver.find_element_by_id('loginAccount').send_keys('13140023070')
driver.find_element_by_id('loginPassword').send_keys('li1548790965')
sleep(2)
driver.find_element_by_xpath('/html/body/div/div/div[2]/form/button').click()
sleep(5)
driver.get('https://www.yyddd.com/pc/#page/clist?sub=0')
##driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/ul/li[5]/ul/li[1]/a/span').click()
sleep(8)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/button').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/ul/li[1]/a').click()
sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[1]/div/div/div/div/div[2]/div/p/button').click()
sleep(5)
os.system("D:\\upfile.exe")