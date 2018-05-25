# Take user input
wrd = input("please enter a word.")

if (len(wrd)%2) is 0:
	
	halfeven = int(len(wrd)/2)
	prefixeven = str(wrd[0:halfeven])
	suffixeven = str(prefixeven[::-1])
	
	if (wrd.startswith(prefixeven, 0, halfeven)) and (wrd.endswith(suffixeven, halfeven, len(wrd))):
		print("This word is a palindrome!")
	else:
		print("This word is NOT a palindrome!")

elif (len(wrd)%2 )is not 0:
	
	halfodd = int((len(wrd)/2))
	prefixodd = str(wrd[0:halfodd])
	suffixodd = str(prefixodd[::-1])
	if (wrd.startswith(prefixodd, 0, halfodd)) and (wrd.endswith(suffixodd, halfodd, len(wrd))):
		print("This word is a palindrome!")
	else:
		print("This word is NOT a palindrome!")

#first part takes input, divides length of string by 2 (making half) 
#that half value integer is used as a range for a substring equal to half of said string
#then, takes that substring and makes string reversed.
		#the two substrings are prefix and suffix, if the word has both, its ruled as a palindrome.
