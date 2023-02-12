from itertools import permutations

def check(first, second, sign):
  if sign == '>':
     return first > second
  else:
     return first < second

numbers = [i for i in range(10)]

n = int(input())
ls = list(input().split())
answer = []
flag = True

for num in permutations(numbers, n+1):
  num_list = list(num)
  for i in range(n):
    if check(num_list[i], num_list[i+1], ls[i]) == False:
      flag = False
      break
  if flag == True:
    answer.append(''.join(map(str, num_list)))
  flag = True

print(answer[-1])
print(answer[0])
