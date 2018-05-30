# Don't delete any of the given code.
def maxBlock(strings):
  count = 0
  tempcount = 1
  # insert your logic here
  for i in range(1, len(strings)):
    if strings[i] == strings[i-1]:
      tempcount +=1
    else:
      tempcount = 1
    if (tempcount > count):
      count = tempcount
  return count
    
  
# Test cases. Don't modify  
print(1,maxBlock("fez day"))   # this would be 2
print(2,maxBlock("day fez"))   # this would be 3
print(3,maxBlock("hoopla"))	  # this would be 0
print(4,maxBlock("abbCCCddBBBxx"))	
print(5,maxBlock(""))	
print(6,maxBlock("xyz"))	
print(7,maxBlock("xxyz"))	
print(8,maxBlock("xyzz"))	
print(9,maxBlock("abbbcbbbxbbbx"))	
print(10,maxBlock("XXBBBbbxx"))	
print(11,maxBlock("XXBBBBbbxx"))	
print(12,maxBlock("XXBBBbbxxXXXX"))
print(12,maxBlock("XX2222BBBbbXX2222"))
