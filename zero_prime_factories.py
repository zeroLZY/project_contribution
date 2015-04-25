import math

#input: number
#output: True  for prime
#		 False for non-prime
def is_prime(number):
	if number <=1 or type(number) == type(0.0):
		return False
	for i in range(2,int(math.sqrt(number))+1):
		if number%i == 0:
			return False
	return True

#input : nmax
#output: a list of prime in range of nmax
def generator_prime_list(nmax):
	prime_list = []
	for i in range(2,nmax+1):
		if is_prime(i):
			prime_list.append(i)

	return prime_list

#input : number
#output: prime factories numbers
def prime_facotories(number):
	prime_list = generator_prime_list(number)
	result =[]
	"""
	for prime_number in prime_list:
		if number%prime_number == 0:
			result.append(prime_number)
			number /= prime_number
			prime_facotories(number)
	I got confused when it comes to global variables in recursive function
	So, I switch to loop strategy.
			"""
	for i in range(1,int(math.sqrt(number))+1):
		for prime_number in prime_list:
			if number%prime_number==0:
				number /=prime_number
				result.append(prime_number)
	result.sort()
	return result

def ans_display(aList):
	for i in range(len(aList)):
		if i == len(aList)-1:
			flag = ''
		else:
			flag = '*'
		print aList[i],flag,


if __name__ == '__main__':
	while True:
		num = input('\n please input a number or \'quit\' for quit:')
		if num:
			result = prime_facotories(num)
			print '>>>',
			ans_display(result)
		if num=='quit':
			break
