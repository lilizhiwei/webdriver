from selenium import webdriver  
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from usedata import get_webinfo,get_userinfo


def get_ele_times(driver,times,func):
	return WebDriverWait(driver,times).until(func)

def openBrower():
	x = webdriver.Firefox()
	return x

def openUrl(handle,url):
	handle.get(url)
	handle.maximize_window()

def findElement(d,arg):
	ele_login = get_ele_times(d,10,lambda d : d.find_element_by_link_text(arg['text_id']))
	ele_login.click()
	userEle = d.find_element_by_id(arg['userid'])
	pwdEle = d.find_element_by_id(arg['pwdid'])
	loginEle = d.find_element_by_id(arg['loginid'])
	a=[userEle,pwdEle,loginEle]
	return a

def sendVals(eletuple,arg):
	listkey = ('uname','pwd')
	i = 0
	for key in listkey:
		eletuple[i].send_keys(' ')
		eletuple[i].clear()
		eletuple[i].send_keys(arg[key])
		i += 1
	eletuper[2].click()

def login_text():
	d = openBrower()
	openUrl(d,url)
	ele_dict = {'text_id':'登录','userid':'id_account_l','pwdid':'id_password_l','loginid':'login_btn'}
	account_dict = {'uname':user,'pwd':pwd}
	ele_tuple = findElement(d,ele_dict)
	sendVals(ele_tuple,account_dict)
	d.quit()
if __name__ == '__main__':
	url = 'http://www.maiziedu.com/'
	login_text = '登录'
	account = '13140023070'
	pwd = 'li1548790965'

	ele_dict = get_webinfo(r'C:\Users\Administrator\webdriver\代码\dingwei.txt')
	user_list = get_userinfo(r'C:\Users\Administrator\webdriver\代码\yonghu.txt')
	login_text(ele_dict,user_list)
