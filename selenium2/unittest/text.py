from calcutor import Count
import unittest

#Tab键与空格键不能混用

class TestCount(unittest.TestCase):
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

if __name__ == '__main__':
#直接unittest.main()为执行该模块内以"test"开头的所有测试方法
	suite = unittest.TestSuite()
	suite.addTest(TestCount("test_add2"))
	runner = unittest.TextTestRunner()
	runner.run(suite)

