
#This program will take an input and give you the coded version
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = int(input('Enter the key shift:'))
newMessage = ''
message= input('\nEnter your message: ')
for character in message:
	if character in alphabet:
		position = alphabet.find(character)
		newPosition = (position + key) % 26
		newCharacter = alphabet[newPosition]

		newMessage += newCharacter
else:
	newMessage += character
print(newMessage)
	
