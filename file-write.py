my_file = open("Multiples.txt", "a")

for z in range(2,13):
	z_str = str(z)
	my_file.write(z_str + " TIMES TABLE\n")
	for x in range(0,12):
		y = int( x * z)
		y_str = str(y)
		x_str = str(x)
		to_write = x_str+ " x " + z_str + " = "+y_str+ "\n"
		my_file.write(to_write)

	
	
	
my_file.close()
