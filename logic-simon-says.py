t = int(input())
tempar = []
for i in range(t):
  init_ = str(input())
  tempar.append(init_)
for x in tempar:
  if x.startswith("simon says") and len(x) > 10:
    print(x[10::])
