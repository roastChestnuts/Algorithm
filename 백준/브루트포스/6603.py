from itertools import combinations

while True:
  num = list(map(int, input().split()))
  k = num[0]
  if k == 0:
    break
  s = num[1:k+1]

  answer = list(combinations(s,6))
  for an in answer:
    for a in an:
      print(a)
  print()