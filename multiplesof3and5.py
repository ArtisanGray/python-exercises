# Use a for loop
add = 0
for x in range(0,500):
	if x%3 == 0 or x%5 ==0:
		add += x
else:
		print(add)
	#First, a sum value (add) is initialized as 0.
	#If number in range is fully divisible by 5 or 3
	#the sum value(add) is then not equaled to, but added to by x's value
	#the reason the else exists is to be an ending to the for loop. When 
	#that ends, it goes through a end condition, instead of just repeating the same number till it hits the end.
	#it then prints the final sum.
