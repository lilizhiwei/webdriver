from selenium import webdriver
from public import Login

driver = webdriver.Firefox()
driver.implcitly_wait(10)
driver.get("https://www.126.com")
#调用登录
Login().user_login(driver)
#测试用例
...
#调用退出
Login().user_logout(driver)