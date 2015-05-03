#**Pig Latin** - 
#Pig Latin is a game of alterations played on the English language game. 
#To create the Pig Latin form of an English word the initial consonant sound 
#is transposed to the end of the word and an ay is affixed 
#(Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules. 

#Rules:
#pig       - igpay
#trash     - ashtray
#egg       -eggway

def Pig_Latin(astring):
	vowel = 'aeiou'
	two_consonant = ['tr','dr','ch','sh','ph','th','qu']

	if astring[0] in vowel:
		return astring+'way'
	else:
		first_two = astring[0:2]
		if first_two in two_consonant:
			return astring[2:]+first_two+'ay'
		else:
			return astring[1:]+astring[0]+'ay'



print Pig_Latin('banana')
print Pig_Latin('orange')
print Pig_Latin('trash')
print Pig_Latin('oodles')
