from itertools import combinations

n, s = map(int, input().split())

num_list = list(map(int, input().split()))
count = 0

for i in range(1, n+1):
   for num in combinations(num_list, i):
     if sum(num) == s:
       count+=1
print(count)      