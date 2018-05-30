# Example code showing how to define a dictionary and add a new key/value pair to it


# Example code showing how to iterate over the keys and values in a dictionary


# >>>>>>>>>>  END OF EXAMPLES <<<<<<<<<<<<

# Write your solution for Exercises 1 and 2 below here:
me = {'Name': 'Ethan', 'DOB': '14/7/00', 'Gender':'Male', 'Eye Color': "Brown"}
me['Height'] = '183cm'
# Exercise 1 :
print ("My details")
print(10 * "=")
# Exercise 2:
for x in me:
    print(x, ":", me[x])

# Write your solution for Exercise 3 below here:
def Exercise3():
	print ("Updated Details")
	print(10 * "=")
	me['Name'] = 'Ethan Wayne Greene'
	for x in me:
  	 print(x, ":", me[x])
Exercise3()
# Write your solution for Exercise 4 below here:
def Exercise4():
	print ("Updated Details")
	print(10 * "=")
	me['Shoe Size'] = '12'
	for x in me:
  	 print(x, ":", me[x])
Exercise4()
# Write your solution for Exercise 5 below here:
def Exercise5():
	print ("Updated Details")
	print(10 * "=")
	del me['Eye Color']
	for x in me:
  	 print(x, ":", me[x])
Exercise5()
