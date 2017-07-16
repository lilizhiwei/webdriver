from selenium import webdriver
from time import *

driver = webdriver.Firefox()
driver.get("https://lilizhiwei.github.io/test-page/DDT-html/xinxi.html")
sleep(2)

a = driver.find_elements_by_xpath("//tr")
sleep(2)

print(len(a))

DW = []
YZ = []

for x in range(len(a)):
	DW.append(driver.find_element_by_xpath("//tr['%s'+1]/td" % x).text)
	YZ.append(driver.find_element_by_xpath("//tr['%s'+1]/td[2]" % x).text)

print(DW)
print(YZ)
