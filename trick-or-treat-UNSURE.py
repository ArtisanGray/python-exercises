x = []
for n in range(0,100):
  if n == 3:
    x.append("Trick")
  if n == 5:
    x.append("Treat")
  while  n > 5 and n != 0:
    if n%5 != 0 or n%3 != 0:
      print(n)
 
    if n%5 == 0:
      x.append("Treat")
    if n%3 == 0:
      x.append("Trick")
    if n%3 and n%5 == 0:
      x.append("Trick or Treat!")
