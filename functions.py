# import anything necessary here.
# A1 - combining inputs
# This program reads three numbers and prints their sum:


def sum_three():
	print("This function prints the sum of three numbers entered by the user.")
	a = int(input("Enter variable a:"))
	b = int(input("Enter variable b:"))
	c = int(input("Enter variable c:"))
	return (a+b+c)
print(sum_three())

#A2 - Area of a Triangle
def tri_area():
	print("This function prints the area of the triangle, based on the user's input of the height and base values.")
	b = int(input("Enter the triangle's base value:"))
	h = int(input("Enter the triangle's height value:"))
	print (b*h/2)
tri_area()
#A3 - Combining Strings
def combine_string():
	print("This function prints and combines a string with a different string contained in a print statement.")
	name =input()
	print("Hello, "+ name + "!")
combine_string()

#A4 - Find the larger of 2 numbers
def num_compare():
	print("This function compares two numbers, and prints the bigger of the two.")
	numA = input()
	numB = input()
	#<<By Ethan Greene>>	
	# Check to see which one is bigger
	if (numA < numB):
	     print('the bigger number is ' + numB)
	elif (numA > numB):
	     print('the bigger number is ' + numA)
	elif (numA == numB):
  	   print('These numbers are equal.')
num_compare()


#A5 - Printing Arrays
def print_arr():
# This is an array that contains different foods
  food_items = ["turkey","ham", "spam","eggs","nuts"]
  print(food_items[3])
# print "eggs" from the loop USING an Array
  for index in food_items:
	  print(index)
print_arr()

	


#A6 - Else if statements
def el_if():
  # This program will take a numerical grade and give a letter grade output
  grade = int(input("Enter your grade: "))
  if (grade >= 90) and (grade <=100):
    print("A")
  elif (grade >=80)and(grade <=89):
    print("B")
  elif(grade >=70)and(grade <=79):
    print("C")
  elif(grade >=60)and(grade <= 69):
    print("D")
  else:
    print("F")
el_if()
# Use an else if statement to check for each letter grade


#A7 - Partial Arrays
def part_arr():
  # Given is the array below.
  a1 = [1, 1, 2, 3, 4, 5, 8, 11, 13, 17, 19, 20, 21, 34, 43, 55, 89]
  for scan in range(len(a1)):
    if (a1[scan] < 30):
      print(a1[scan])
      
part_arr()

#Print out all elements of the array that are less than 30







