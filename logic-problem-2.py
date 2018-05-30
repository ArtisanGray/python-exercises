# Don't delete any of the given code.

def scoresIncreasing(scoresList):
  isCorrect = False
  # insert your logic here
  for i in range(len(scoresList)-1):
 
    if scoresList[i+ 1] >= scoresList[i]:
      isCorrect = True
    else:
      return False
  return isCorrect
# Test cases. Don't modify  
print(1,scoresIncreasing([1, 3, 4]))   # this would be True
print(2,scoresIncreasing([1, 3, 2]))   # this would be False
print(3,scoresIncreasing([1, 1, 4]))   # this would be True
print(4,scoresIncreasing([1, 1, 2, 4, 4, 7]))
print(5,scoresIncreasing([1, 1, 2, 4, 3, 7]))
print(6,scoresIncreasing([-5, 4, 11]))
