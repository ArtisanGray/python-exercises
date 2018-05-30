#I did this a completely different way. Oof.
import random

print('='*40)
print("Welcome to Rock, Paper, Scissors!")
print('='*40)
print()

player = input("Please enter Rock, Paper, or Scissors:")
choices = ['Rock',"Paper","Scissors"]
x = random.randint(0,2)
player2_play =  choices[x]
print ("Player 2 plays " + choices[x])
if player2_play == choices[0] and player == choices[0]:#R vs R
  print("It's a tie!")
elif player2_play == choices[1] and player == choices[1]:#P vs P
  print("It's a tie!")
elif player2_play == choices[2] and player == choices[2]:#S vs S
  print("It's a tie!")
elif  player2_play == choices[0] and player == choices[2]:#R vs S
  print("Player_Bot wins!")
elif player2_play == choices[1] and player == choices[2]:#P vs S
  print("Player 1 wins!")
elif player2_play == choices[0] and player == choices[1]:#R vs P
  print("Player 1 wins!")
elif  player2_play == choices[2] and player == choices[1]:#S vs P
  print("Player_Bot wins!")
elif  player2_play == choices[1] and player == choices[0]:#P vs R
 print("Player_Bot wins!")
elif  player2_play == choices[2] and player == choices[0]:#S vs R
 print("Player 1 wins!")

