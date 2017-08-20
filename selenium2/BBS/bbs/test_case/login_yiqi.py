from selenium import webdriver
from time import sleep
import unittest,sys
sys.path.append("./page_obj")
from page_obj.loginPage import login

class loginTest(unittest.TestCase):
	'''社区登录测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()

	#测试用户登录
	def user_login_verify(self,username="",password=""):
		login(self.driver).user_login(username,password)

	def test_login1(self):
		'''用户名、密码为空'''
		self.user_login_verify()
		po = login(self.driver)
		sleep(1)
		self.assertEqual(po.user_error_hint(),"请填写完整的登录信息")
		self.assertEqual(po.pawd_error_hint(),"请填写完整的登录信息")

		'''用户名正确、密码为空'''
		self.user_login_verify(username="pytest")
		po = login(self.driver)
		sleep(1)
		self.assertEqual(po.pawd_error_hint(),"请填写完整的登录信息")

		'''用户名为空、密码正确'''
		self.user_login_verify(password="abc123456")
		po = login(self.driver)
		sleep(1)
		self.assertEqual(po.user_error_hint(),"请填写完整的登录信息")

		'''用户名、密码不匹配'''
		self.user_login_verify(username="username",password="123456")
		po = login(self.driver)
		sleep(1)
		self.assertEqual(po.pawd_error_hint(),"请点击按钮进行验证")

		'''用户名、密码都正确'''
		self.user_login_verify(username="zhangsan",password="123456")
		po = login(self.driver)
		sleep(1)
		self.assertEqual(po.user_login_success(),'请点击按钮进行验证')

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()


