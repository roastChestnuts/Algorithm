mushrooms = [int(input()) for _ in range(10)]
dp = []
answer = 0

for i in range(1, 10):
    mushrooms[i] += mushrooms[i-1]

for mushroom in mushrooms:
  dp.append(abs(100 - mushroom))

for mushroom in mushrooms:
  if min(dp) == abs(100 - mushroom):
    answer = max(answer, mushroom)

print(answer)