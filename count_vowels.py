#encoding=utf-8
#**Count Vowels** - 
#Enter a string and 
#the program counts the number of vowels in the text. 
#For added complexity have it report a sum of each vowel found. 

vowels = 'aeiou'



def count_vowels(aString):
	dict_vowels = {}
	for char in aString:
		if char in vowels:
			dict_vowels[char] = 1 + dict_vowels.get(char, 0)
	return dict_vowels

#test
print count_vowels('are you ok sir')
