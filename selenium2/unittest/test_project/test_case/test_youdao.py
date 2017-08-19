from selenium import webdriver
import unittest
import time

class MyTest(unittest.TestCase):
	'''有道搜索测试'''
	
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(10)
		self.base_url = 'https://www.baidu.com'

	def test_baidu(self):
		driver = self.driver
		driver.get(self.base_url + '/')
		time.sleep(2)
		driver.find_element_by_id('kw').send_keys('webdriver')
		driver.find_element_by_id('su').click()
		time.sleep(2)
		self.assertEqual(driver.title,"webdriver_百度搜索")
		time.sleep(2)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()
