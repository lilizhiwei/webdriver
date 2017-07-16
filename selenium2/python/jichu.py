# coding=utf-8

#输出

name = "zhangsan"
print("hello %s!" %name)

age = 14
print("hello %d!" %age)

print("hello %d+%s!" %(age,name))

print("hello")
print('hello')

#判断
a = 52
if a >= 90:
	print('优秀')
elif a >= 70:
	print('良好')
elif a >= 60:
	print('及格')
else:
	print('不及格')

#循环

for x in range(10):
	print(x)
for i in range(1,10,2):
	print(i)

#数组
list = [1,2.34,5.6]
print(list[0])

#字典
dict = {'username':'zhangsan','password':'123456'}
print(dict)
print(dict.keys())
print(dict.items())
print(dict.values())

#函数

def add(a=1,b=2):
	print(a+b)
add()
add(2,3)

#类和方法

class A(object):
	"""docstring for A"""
	def add(self,a,b):
		return a+b
		
class B(A):
	"""docstring for B"""
	def sub(self, a,b):
		return a - b
print(B().add(4,5))						
print(B().sub(4,5))						

#引用模块

import time
print(time.ctime())

from time import *
sleep(2)
print(ctime())

#异常

try:
	#aa=2
	print(aa)
except Exception as e:
	print(e)
else:
	print('无异常')
finally:
	print('少不了的我')
