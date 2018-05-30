import random

print('Welcome to Hangman!')


# Insert the code from last exercise here.    
def hangman():
  with open('wordbank.txt', 'r') as f:
   lines = f.readlines()
   word = (lines[random.randint(0,len(lines))])
hangman()


# Now ask the user to guess the wordguess = list('_')
guess = list('_'*len(word))
while list(word) != guess:
  print(' '.join(guess))  # This joins the guess with the blank spaces.
  
  #Step 3
