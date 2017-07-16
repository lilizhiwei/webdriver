from calcutor import Count
import unittest

#Tab键与空格键不能混用

class TestAdd(unittest.TestCase):
	def setUp(self):
		print("test start")
	def test_add(self):
		j = Count(2,3)
		self.assertEqual(j.add(),5)
	def test_add2(self):
		j = Count(41,76)
		self.assertEqual(j.add(),117)
	def tearDown(self):
		print("test end")

class TestSub(unittest.TestCase):
	def setUp(self):
		print("test start")
	def test_sub(self):
		j = Count(2,3)
		self.assertEqual(j.sub(),-1)
	def test_sub2(self):
		j = Count(41,76)
		self.assertEqual(j.sub(),-35)
	def tearDown(self):
		print("test end")

if __name__ == '__main__':
#直接unittest.main()为执行该模块内以"test"开头的所有测试方法
	suite = unittest.TestSuite()
	suite.addTest(TestAdd("test_add"))
	suite.addTest(TestAdd("test_add2"))
	suite.addTest(TestSub("test_sub"))
	suite.addTest(TestSub("test_sub2"))
	runner = unittest.TextTestRunner()
	runner.run(suite)

