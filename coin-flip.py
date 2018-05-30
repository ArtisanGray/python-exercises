import random
user = input('How many times do you want to flip a coin?\n')
num = int(user)
heads = int(0)
tails = int(0)
for x in range(0,num):
  flip = random.randint(0,1)
  if flip == 0:
    heads += 1
  elif flip == 1:
    tails += 1
else:
  print("Total coin flips")
  print("="*12)
  print("Heads: "+ str(heads))
  print("Tails: "+ str(tails))
  

