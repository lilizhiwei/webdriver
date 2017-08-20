import unittest,time
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
	now = time.strftime("%Y-%m-%d %H-%M-%S")
	filename = './bbs/report/' + now + 'result.html'

	fp = open(filename,'wb')
	runner = HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况')

	discover = unittest.defaultTestLoader.discover('./bbs/test_case',pattern='login_*.py')
	runner.run(discover)
	fp.close()