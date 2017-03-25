import codecs

def get_webinfo(path):
	user_info = {}
	config = codecs.open(path,'r','utf-8')
	for line in config:
		result = [ele.strip() for ele in line.split('=')]
		web_info.updata(dict([result]))
	return web_info

def get_userinfo(path):
	user_info = []
	config = codecs.open(path,'r','utf-8')
	for x in config:
		user_dict = {}
		result = [ele.strip() for ele in x.sprit(' ')]
		for r in result:
			account = [ele.strip() for ele in r.spilt('=')]
			user_dict.updata(dict([account]))
		user_info.append(user_dict)
	return user_info

