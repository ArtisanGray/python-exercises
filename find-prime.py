num = 600851475143
dividend = 2
PrimeFactors = [ ]
while num > 1:#while initial number is more than 1
  if num % dividend == 0:#if modulated number by divisor is equal to 0:
    PrimeFactors.append(dividend)#appends newest interation of the dividend
    num = num/dividend#new renditon of number is itself/dividend
  else:#if remainder exists, this is called
    dividend = dividend + 1#the dividend is now added to by 1, and run though the While loop again.
PrimeList = sorted(PrimeFactors)#sorts the primes from lowest to highest
print(PrimeList[-1])#prints the largest prime
