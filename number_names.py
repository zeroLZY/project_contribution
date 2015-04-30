#encoding=utf-8
#**Number Names** - Show how to spell out a number in English. 
#You can use a preexisting implementation or roll your own, 
#but you should support inputs up to at least one million 
#(or the maximum value of your language's default bounded integer type, if that's less). 
#*Optional: Support for inputs other than positive integers 
#(like zero, negative integers, and floating-point numbers).*

#最重要的是，如何选择数据结构
#先处理整数部分
#x     xx,     x   x x,     x    xx,     x     xx,
#trillion,     billion,     million,     thousand
def less20_digit2char(digit):
	char = ['zero ','one ','two ','three ','four ','five ','six ','seven ','eight ','nine ',\
			'ten ','eleven ','twelve ','thirteen ','fourteen ','fifteen ','sixteen ',\
			'seventeen ','eighteen ','nineteen ']
	return char[digit]

def more20_tenth2char(digit):
	char = ['twenty ','thirty ','fourty ','fifty ','sixty ','seventy ','eighty ','ninety ']
	choice = (digit-2)
	return char[choice]

def base3digit(number):
	#number is less than 1000
	number_string = ''
	hundred, remaind = number/100, number%100
	if hundred:
		number_string = less20_digit2char(hundred) + 'hundred and '
	if remaind > 20:
		tenth, remaind = remaind/10, remaind%10
		number_string = number_string + more20_tenth2char(tenth)
	number_string = number_string + less20_digit2char(remaind)
	return number_string

def int_number_spellout(number):
	result_string = ''
	#判断其数字的长度，而不是大小
	digit_string = str(number)
	digit_length = len(digit_string)

	if digit_length <=3:
		result_string = base3digit(int(digit_string[0:])) + result_string
	if 3< digit_length <=6:
		result_string = base3digit(int(digit_string[0:digit_length-3])) \
					  + 'thousand '\
					  + base3digit(int(digit_string[digit_length-3:])) + result_string
	if 6 < digit_length <=9:
		result_string = base3digit(int(digit_string[0:digit_length-6]))\
					  + 'million '\
					  +	base3digit(int(digit_string[digit_length-6:digit_length-3])) \
					  + 'thousand '\
					  + base3digit(int(digit_string[digit_length-3:])) \
					  + result_string
	if 9 < digit_length<=12: 
		result_string = base3digit(int(digit_string[0:digit_length-9]))\
					  + 'billion '\
					  +	base3digit(int(digit_string[digit_length-9:digit_length-6]))\
					  + 'million'\
					  +	base3digit(int(digit_string[digit_length-6:digit_length-3])) \
					  + 'thousand '\
					  + base3digit(int(digit_string[digit_length-3:])) \
					  + result_string

	return result_string

def number_spell_out(number):
	result_string = ''

	if number < 0:
		sign_flag = 'minus '
	else:
		sign_flag = ''
	number = abs(number)
	
	string_number = str(number)
	point_index = string_number.find('.')
	#not find, return -1
	if point_index == -1:
		result_string = int_number_spellout(number)
	else:
		int_part = int_number_spellout(int(string_number[0:point_index]))

		frac_list = [less20_digit2char(int(x)) for x in string_number[point_index+1:]]
		frac_part = reduce(lambda x,y: x+y, frac_list)
		result_string = sign_flag + int_part + 'point ' + frac_part
	return result_string

#test
#print number_spell_out(-123.345)


if __name__ == '__main__':
	while True:
		number = input('Enter a number or \'quit\' for stop the program: ')
		print type(number),number
		if str(number) == 'quit':
			exit()
		else:
			print number_spell_out((number))
