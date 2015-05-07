def is_palindrome(s):
	s = str(s)
	if len(s) == 0 or len(s) == 1:
		return True
	elif s[0] == s[-1]:
		s = s[1:-1]
		return True and is_palindrome(s)
	else:
		return False
#test
print is_palindrome('n')
