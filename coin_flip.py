#encoding=utf-8
#**Coin Flip Simulation** - 
#Write some code that simulates flipping a single coin however many times the user decides. 
#The code should record the outcomes and count the number of tails and heads.

#dict : record every outcomes
#int number for number of tails or heads

import random
#print random.randint(1,100)
#low and high, including both
class record_coin_flip(object):
	def __init__(self,nmax):
		self.number = nmax
		self.record_dict = {}
		self.tail = 0
		self.head = 0

	def start_flip(self):
		for i in range(self.number):
			result = random.randint(1,100)
			if result%2:
				self.record_dict[i+1] = 'tail'
				self.tail +=1
			else:
				self.record_dict[i+1] = 'head'
				self.head +=1
	def show(self):
		print self.record_dict
	def show_tail(self):
		print ('tail times: ',self.tail)
	def show_head(self):
		print ('head times: ',self.head)


zero = record_coin_flip(10)
zero.start_flip()
zero.show()
zero.show_tail()
zero.show_head()
#用时12:25s结束






