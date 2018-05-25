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
# Use an else if statement to check for each letter grade
