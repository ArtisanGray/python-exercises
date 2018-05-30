#was this a "playground" program just to get us used to using global and local varibles?

#If so...
x = 1

def add():
	global x
	print(x + 3)
	
add()
