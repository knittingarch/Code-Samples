''' Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. '''

from string import maketrans, ascii_letters

def LetterChanges(str): 
	char_incrementer = maketrans(ascii_letters, ascii_letters[1:]+ascii_letters[0])
	str = str.translate(char_incrementer)
	vowels = "aeiou"
    	for vowel in vowels:
			str = str.replace(vowel, vowel.upper())
			return str    

print LetterChanges('All aboard the 5pm train to Dance City!')    