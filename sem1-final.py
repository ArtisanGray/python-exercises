def PythagoreanTheroem(a, b, c):
  if c**2 < (a**2 + b**2):
    print("Acute")
  elif c**2 == (a**2 + b**2):
    print("Right")
  elif c**2 > (a**2 + b**2):
    print("Obtuse")
#while True:
side_int = input().split()
PythagoreanTheroem(int(side_int[0]),int(side_int[1]), int(side_int[2]))
#in order to pass the tests, i had to remove the input prompt string.
