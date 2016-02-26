'''Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. 
'''

def LongestWord(sen): 
	for char in sen:
		if not char.isalnum():
			sen = sen.replace(char, ' ')
	word = sen.split()
	word.sort(key = lambda x: len(x))
	return 	word[-1] 
    
# keep this function call here  
print LongestWord("a beautiful sentence^&!")           
