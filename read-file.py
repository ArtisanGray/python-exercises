message_file = open('alice.txt','r')
line_counter = 0#initializes the count parameter
words_to_change = {"Alice":"Bob", "she":"he", "Lewis Carroll":"Ethan Greene"}
for line in message_file:
	for word in words_to_change:
		line = line.replace(word, words_to_change[word])
		print(line, end="")	
		line_counter+= 1
		if line_counter == 20:
			usr_input = input("press Enter to print another 20 lines")
			line_counter -= 20
message_file.close()
