import random

def hangman():
  with open('wordbank.txt', 'r') as f:
   lines = f.readlines()
   print(lines[random.randint(0,len(lines))])
hangman()
