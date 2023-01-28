from itertools import permutations

n, m = map(int, input().split())
list = [i for i in range(1, n+1)]

ans = permutations(list, m)

for i in ans:
    for j in i:
        print(j, end = ' ')
    print()

#########################################
#백트래킹 이용

n, m = map(int, input().split())
list = [i for i in range(1, n+1)]
ans = []

def func():
    if len(ans) == m:
        print(*ans)
        return
    for i in list:
        if i not in ans:
            ans.append(i)
            func()
            ans.pop()
func()          