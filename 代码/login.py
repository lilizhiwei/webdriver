from selenium import webdriver  

import time

url = 'http://www.maiziedu.com/'
user = '13140023070'
pwd = 'li1548790965'

def login_text():
	d = webdriver.Firefox()
	d.get(url)
	time.sleep(5)
	d.maximize_window()
	time.sleep(1)
	d.find_element_by_link_text('登录').click()
	time.sleep(1)
	user1 = d.find_element_by_id('id_account_l')
	time.sleep(1)
	pwd1 = d.find_element_by_id('id_password_l')
	user1.clear()
	user1.send_keys(user)
	pwd1.clear()
	pwd1.send_keys(pwd)
	d.find_element_by_id('login_btn').click()
	try:
		d.find_element_by_link_text('该账号格式不正确') # 错误，该字体不是超链接，出现了也捕获不到
		print('ERROR')
	except:
		print('RIGHT')
	d.close()

if __name__ == '__main__':
	login_text()
	time.sleep(2)
