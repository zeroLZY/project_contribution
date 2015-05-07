#encoding=utf-8
#**Count Words in a String** - 
#Counts the number of individual words in a string. 
#For added complexity read these strings in from a text file 
#and generate a summary.

def count_words_string(aString):
	dict_word = {}
	sign = '.,-!@#$%^&*()+={}[]|\\;:\"<>'
	bString = aString.lower()
	# remove signs in a sentence
	for char in bString:
		if char in sign:
			bString = bString.replace(char,'')

	word_list = bString.split()
	for word in word_list:
		dict_word[word] = 1+ dict_word.get(word,0)
	return dict_word

print count_words_string('Counts the number of of individual words in a string. I am good of man.')
