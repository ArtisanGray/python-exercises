#check how to read and open a file from A20
my_file = open("alice.txt", "r")

#create a function to count a specified word
#Please change the example words

def CountWord(my_file, str_1):
	
	count = int(0)
	str_1 = str()
	for line in my_file:
		if str_1 in line:
			count+= 1
	print(count)
CountWord("alice.txt", "Alice")
