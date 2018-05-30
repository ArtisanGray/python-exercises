#Ask the user what size of game board do they want to print?
board_size = int(input("What size of game board? "))

def print_horiz_line():
  x = 0
  print(" ---" * board_size)
def print_vert_line():
  z = 0
  print("|   "*(board_size + 1))
for y in range(0,board_size):
  print_horiz_line()
  print_vert_line()
else:
  print_horiz_line()#prints the bottom line of the board when finished with the for loop
