#encoding=utf-8
#**Reverse a String** - 
#Enter a string and the program will reverse it and print it out.

def reverse_string(aString):
	return aString[::-1]

if __name__ == '__main__':
	while True:
		string = raw_input('Enter a string: ')
		if string == 'quit':
			break
		else:
			print reverse_string(string)
