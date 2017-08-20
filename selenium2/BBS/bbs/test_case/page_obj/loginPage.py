from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import unittest

class login(object):
	'''用户登录页面'''

	bbs_url = 'https://bbs.meizu.cn'
	url = '/'

	def __init__(self, selenium_driver,base_url=bbs_url):
		self.base_url = base_url
		self.driver = selenium_driver
		self.timeout = 30

	def open(self,url):
		url = self.base_url + url
		self.driver.get(url)


	def bbs_login(self):
		self.driver.find_element_by_xpath("//div[@id='mzCust']/div/div/img").click()
		sleep(1)
		self.driver.find_element_by_id("mzLogin").click()

	#填写用户名
	def login_username(self,username):
		self.driver.find_element_by_id("account").send_keys(username)

	#填写密码
	def login_password(self,password):
		self.driver.find_element_by_id("password").send_keys(password)

	#点击登录按钮
	def login_button(self):
		self.driver.find_element_by_id("login").click()

	#定义统一登录入口
	def user_login(self,username="username",password="1111"):
		'''获取的用户密码登录'''
		self.open(self.url)
		self.bbs_login()
		self.login_username(username)
		self.login_password(password)
		self.login_button()
		sleep(1)

	user_error_hint_loc = (By.XPATH,"//span[@for='account']")
	pawd_error_hint_loc = (By.XPATH,"//span[@for='password']")
	user_login_success_loc = (By.ID,"mzCustName")

	#用户名错误提示
	def user_error_hint(self):
		return self.find_element(*self.user_error_hint_loc).text

	#密码错误提示
	def pawd_error_hint(self):
		return self.find_element(*self.pawd_error_hint_loc).text

	#登录成功提示
	def user_login_success(self):
		return self.find_element(*self.user_login_success_loc).text
