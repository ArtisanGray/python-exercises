import random #this will import a random number

num = random.randint(1, 100)
print(num)
guess = int(input("Guess a number: "))
if guess == num:
	print("Correct!")
elif guess > (num + 10):
		print ("Nope! Too High!")
elif guess < (num - 10):
		print ("Nope! Too Low!")
else:
		print("Nope!")
