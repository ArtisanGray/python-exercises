word = input("In: ")
vowels = ["a","e","i","o","u"]
vowel_int = 0
word_str = list(word)
y = 0
for x in range(0, len(word)):
  for y in range(0,5):
    if vowels[y] == word[x]:
      vowel_int += 1
      
else:
  revise = int(len(word) - vowel_int)
  print(revise)
