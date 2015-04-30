#encoding=utf-8
#**Collatz Conjecture** - 
#Start with a number *n > 1*. 
#Find the number of steps it takes to reach one using the following process: 
#If *n* is even, divide it by 2. If *n* is odd, multiply it by 3 and add 1

#input : number n
#output: how many steps to be 1


def find_steps(n,depth=0):
	if n == 1:
		return depth
	else:
		depth += 1
		if n%2 == 0:
			n = n/2
		else:
			n = 3*n + 1
	return find_steps(n,depth)

if __name__ == '__main__':
	while True:
		number = input('Enter your test number:')
		print int(number),' need ',find_steps(int(number)),' steps to be 1.'
