n, s = map(int, input().split())
numbers = list(map(int, input().split()))
count = 0
tmp = []

def backtrack(start):
    global count
    if len(tmp) > 0 and sum(tmp) == s:
        count += 1
      
    for i in range(start, n):
        tmp.append(numbers[i])
        backtrack(i+1)
        tmp.pop()
backtrack(0)
print(count)

# from itertools import combinations

# n, s = map(int, input().split())

# num_list = list(map(int, input().split()))
# count = 0

# for i in range(1, n+1):
#    for num in combinations(num_list, i):
#      if sum(num) == s:
#        count+=1
# print(count)      