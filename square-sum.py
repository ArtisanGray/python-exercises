
# Print answers
print('The difference is: ' )
array = []
array2 = []
for i in range(0,101):
  sq = (i*i)
  array2.append(i)
  array.append(sq)
sum_ = int(sum(array))
sum_2 = int(sum(array2))
print((sum_2*sum_2)-sum_)
