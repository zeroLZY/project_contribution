#encoding=utf-8
#**Limit Calculator** - 
#Ask the user to enter f(x) and the limit value, 
#I think 'the limit value' means x
#then return the value of the limit statement 
#*Optional: Make the calculator capable of supporting infinite limits.*

#eval()
#lambda
from math import *
def limit_calculator():
	fx      = raw_input('Enter your function f(x):')
	x_limit = input('Enter x limit value:')
	f_x = lambda x:eval(fx)
	miu = 0.00000000000001
	if f_x(x_limit + miu) == f_x(x_limit - miu):
		print f_x(x_limit + miu)

if __name__ == '__main__':
	limit_calculator()

#state: complete.
