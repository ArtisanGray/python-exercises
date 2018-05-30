#get words as an input
anagram = input('Welcome to Scrabble Hax! \n Enter a word to hax!:\n').upper()
list_anagram = list(anagram)
print (list_anagram)
list_anagram.sort()
print(list_anagram)

def check_words(filename = 'wordbank.txt'):
  with open(filename) as f:
    for line in f:#For a line in a file,
      word = line.strip()
      list_word = list(word)
      list_word.sort()
      if list_word == list_anagram:
        print(word)
        
check_words()
  
