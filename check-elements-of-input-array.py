# Use your code from the last exercise.


# Now check to see how many of a number are in the array.
# Hint: use the code from the examples in class.

# Use your code from the last exercise.
numbers = []
input_len = int(input("How many elements do you want?: ") )


# Now use a for loop to add to the array.
for index in range(0, input_len):
	input_add = int(input("Enter next number: "))
	numbers.append(input_add)
else:
	print(numbers)

	
count = 0		
print("Enter a number 0 - 9:")
elem = int(input("Which number do you want to find?"))
for index in range(0,input_len):
	if numbers[index] == elem:
		count+=1
else:
	print("There are " , count, elem,"'s in the array")
