# Don't delete any of the given code.

def countYZ(strings):
  isend = 0
  prev = ""
  # insert your logic here
  for char in strings:
    
    i = char.isalpha()
    if i ==False:
        if prev =="y" or prev == "z":
          isend +=1
    prev = char.lower()
  if prev == "y" or prev == "z":
    isend += 1
  return isend
# Test cases. Don't modify  
print(1,countYZ("fez day"))   # this would be True
print(2,countYZ("day fez"))   # this would be False
print(3,countYZ("day fyyyz"))   # this would be True
print(4,countYZ("day yak"))
print(5,countYZ("day:yak"))
print(6,countYZ("!!day--yaz!!"))
print(7,countYZ("yak zak"))
print(8,countYZ("DAY abc XYZ"))
print(9,countYZ("aaz yyz my"))
print(10,countYZ("y2bz"))
print(11,countYZ("zxyx"))
