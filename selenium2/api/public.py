class Login(object):
		
	def  user_login(self,driver):
		driver.find_element_by_id("idInput").clear()
		driver.find_element_by_id("idInput").send_keys("username")
		driver.find_element_by_id("pwdInput").clear()
		driver.find_element_by_id("pwdInput").send_keys("password")
	    driver.find_element_by_id("loninBtn").click()

	def user_logout(self,driver):
		driver.find_element_by_link_text("退出").click()
		driver.quit()
