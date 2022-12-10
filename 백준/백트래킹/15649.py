from itertools import permutations

n, m = map(int, input().split())
list = [i for i in range(1, n+1)]

ans = permutations(list, m)

for i in ans:
    for j in i:
        print(j, end = ' ')
    print()