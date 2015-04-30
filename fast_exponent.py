#encoding=utf-8
#**Fast Exponentiation** - 
#Ask the user to enter 2 integers a and b 
#and output a^b (i.e. pow(a,b)) in O(lg n) time complexity.
import time
from math import *
def fast_exponentiation(base, index):
	if base == 1:
		return 1
	if index == 1:
		return base

	if base==0 and index == 0:
		return 1
	if base==0 and index !=0:
		return 0
	if base != 0 and index == 0:
		return 1
	else:
		if index > 2:
			if index%2 == 0 :
				index = index/2
				half = fast_exponentiation(base,index)
				return fast_exponentiation(half,2)
			else:
				index = index/2
				half = fast_exponentiation(base,index)
				return fast_exponentiation(half,2)*base
		else:
			return base**index

def slow(base, index):
	result = 1
	for i in range(index):
		result *= base
	return result

time0 = time.time()
print fast_exponentiation(56,100)
time1 = time.time()
print 'fast',time1-time0

print 56**100
time2 = time.time()
print 'common',time2-time1

print pow(56,100)
time3 = time.time()
print 'power:', time3-time2

print slow(56,100)
time4 = time.time()
print 'slow',time4-time3
#经检验，自己的方法并不比** 方法快，而且还慢了不少呢
#值得向别人借鉴方法
