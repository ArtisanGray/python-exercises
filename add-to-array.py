# Create a blank array
numbers = []
input_len = int(input("How many elements do you want?: ") )


# Now use a for loop to add to the array.
for index in range(0, input_len):
	input_add = input("Enter next number: ")
	numbers.append(input_add)
else:
	print(numbers)
