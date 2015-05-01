#encoding=utf-8
#*Happy Numbers** 
#- A happy number is defined by the following process. 
#Starting with any positive integer, replace the number by the sum of the squares of its digits, 
#and repeat the process until the number equals 1 (where it will stay), 
#or it loops endlessly in a cycle which does not include 1. 
#Those numbers for which this process ends in 1 are happy numbers, 
#while those that do not end in 1 are unhappy numbers.
# Display an example of your output here. 
#Find first 8 happy numbers.

#happy number:
#我已经知道为什么了，因为前面错误的数字，影响了deepth，多次使用会叠加

def is_happy_number(number, deepth=0):
	astring = str(number)
	digits = [int(char) for char in astring]
	sum_digit = sum([digit**2 for digit in digits])
	if sum_digit == 1:
		return True
	else:
		deepth += 1
		if deepth >800:
			return False
		return is_happy_number(sum_digit,deepth)

print '7',is_happy_number(7,0)

for number in range(1,100):
	if is_happy_number(number,0):
		print number,
