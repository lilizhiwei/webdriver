from selenium import webdriver
import unittest
import time

class MyTest(unittest.TestCase):
	'''有道搜索测试'''
	
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.implicitly_wait(10)
		self.base_url = "http://www.youdao.com"

	def test_baidu(self):
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_id('query').clear()
		driver.find_element_by_id('query').send_keys('webdriver')
		driver.find_element_by_id('qb').click()
		time.sleep(2)
		self.assertEqual(title,"webdriver_有道搜索")

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()
