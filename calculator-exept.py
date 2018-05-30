def add(a, b):
  print(a,"+",b,"=", int(a+b))
def sub(a, b):
  print(a,"-",b,"=", int(a - b))
def multi(a, b):
  print(a ,"*", b , "=", int(a*b))
def div(a, b):
  print(a,"/", b, "=", int(a/b))
  
def calc():
  while True:
    try:
      print("Select operation.")
      print("1.Add")
      print("2.Subtract")
      print("3.Multiply")
      print("4.Divide")
      choice = int(input("Enter choice(1/2/3/4):  "))
    except ValueError:
      print("Not an valid input. Try again.")
    else:
      if choice ==1:
        number_a = int(input("Enter first number:  "))
        number_b = int(input("Enter second number:  "))
        add(number_a, number_b)
      if choice == 2:
        number_a = int(input("Enter first number:  "))
        number_b = int(input("Enter second number:  "))
        sub(number_a, number_b)
      if choice == 3:
        number_a = int(input("Enter first number:  "))
        number_b = int(input("Enter second number:  "))
        multi(number_a, number_b)
        break
      if choice == 4:
        number_a = int(input("Enter first number:  "))
        number_b = int(input("Enter second number:  "))
        div(number_a, number_b)
        break
        
calc()
