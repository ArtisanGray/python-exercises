# this is a challenge. don't delete any of the given code.
def make_bricks(small, big, goal):
    totalBB = int(big*5)
    if (goal % 5) <= small and (goal - (totalBB)) <= small:
      return True
      #first half of if statement remainder divides the Goal by the length of a big brick.
      #If the remainder is less than (down to 0) or equal to the number of small bricks, it can be returned True.
     # Second Half of the if statement says if the goal MINUS the total addend of the big bricks is
     # less than the small bricks, these two requisites will return True.
    else:
      return False

  
  
 



# Test cases. Don't modify  
print(1,make_bricks(3, 1, 8))   # this would be True
print(2,make_bricks(3, 1, 9))   # this would be False
print(3,make_bricks(3, 2, 10))  # this would be True.....
print(4,make_bricks(3, 2, 8))
print(5,make_bricks(3, 2, 9))
print(6,make_bricks(6, 1, 11))
print(7,make_bricks(6, 0, 11))
print(8,make_bricks(1, 4, 11))
print(9,make_bricks(0, 3, 10))
print(10,make_bricks(1, 4, 12))
print(11,make_bricks(3, 1, 7))
print(12,make_bricks(1, 1, 7))
print(13,make_bricks(2, 1, 7))
print(14,make_bricks(7, 1, 11))
print(15,make_bricks(7, 1, 8))
print(16,make_bricks(7, 1, 13))
print(17,make_bricks(43, 1, 46))
print(18,make_bricks(40, 1, 46))
print(19,make_bricks(40, 2, 47))
print(20,make_bricks(40, 2, 50))
print(21,make_bricks(40, 2, 52))
print(22,make_bricks(22, 2, 33))
print(23,make_bricks(0, 2, 10))
print(24,make_bricks(10000000, 1000, 1000100))
print(25,make_bricks(2, 1000000, 100003))
print(26,make_bricks(20, 0, 19))
print(27,make_bricks(20, 0, 21))
print(28,make_bricks(20, 4, 51))
print(29,make_bricks(20, 4, 39))
