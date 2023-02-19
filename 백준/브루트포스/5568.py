from itertools import permutations

n = int(input())
k = int(input())

numbers = list(input() for _ in range(n))
answer = set()

for num in permutations(numbers, k):
  answer.add(''.join(num))

print(len(answer))