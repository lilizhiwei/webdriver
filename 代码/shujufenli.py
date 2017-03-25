from selenium import webdriver  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


url = 'http://www.maiziedu.com/'
login_text = '登录'
account = '13140023070'
pwd = 'li1548790965'

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
	useEle = d.find_element_by_id(arg['userid'])
	pwdEle = d.find_element_by_id(arg['pwdid'])
	loginEle = d.find_element_by_id(arg['loginid'])
	return useEle,pwdEle,loginEle

def sendVals(eletuple,arg):
	listkey = ('uname','pwd')
	i = 0
	for key in listkey:
		eletuple[i].send_keys(' ')
		eletuple[i].clear()
		eletuple[i].send_keys(arg[key])
		i += 1
	eletuper[2].click()

def checkResult(d,text):
	try:
		d.find_element_by_link_text(text)
		print('ERROR')
	except:
		print('RIGHT')

def login_test(ele_dict,user_list):
	d = openBrower()
	openUrl(d,ele_dict['url'])
	
	
	ele_tuple = findElement(d,ele_dict)
	for arg in user_list:
		sendVals(ele_tuple,arg)
		checkResult(d,ele_dict['errorid'])
	
	d.quit()
	
if __name__ == '__main__':
	url = 'http://www.maiziedu.com/'
	login_text = '登录'
	account = '13140023070'
	pwd = 'li1548790965'
	ele_dict = {'url':url,'text_id':'登录','userid':'id_account_l','pwdid':'id_password_l','loginid':'login_btn','errorid':'该账号格式不正确'}
	user_list = [{'uname':account,'pwd':pwd},]
		
	login_test(ele_dict,user_list)



