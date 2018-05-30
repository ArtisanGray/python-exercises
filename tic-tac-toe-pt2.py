
a = [[2, 1, 2], [0, 1, 2], [2, 1, 1]]

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]
	
	
if a[0][1] and a[1][1] and a[2][1] == winner_is_also_1[0][1] and winner_is_also_1[1][1] and winner_is_also_1[2][1]:
  print("You Win!")
elif a[0][0] and a[1][1] and a[2][2] == winner_is_1[0][0] and winner_is_1[1][1] and winner_is_1[2][2]:
  print("You Win!")
elif a[0][0] and a[1][1] and a[2][1] == no_winner[0][0] and no_winner[1][1] and no_winner[2][1]:
  print("No One Wins!")
elif a[0][2] and a[1][2] and a[2][2] == also_no_winner[0][2] and also_no_winner[1][2] and also_no_winner[2][2]:
  print("No One Wins!")
else:
  print("Player 2 Wins!")
