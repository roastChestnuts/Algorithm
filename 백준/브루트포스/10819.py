ans = []
n = int(input())
numbers = list(map(int, input().split()))
used = [True for _ in range(n)]
answer = 0

def count():
    num = 0
    for i in range(n-1):
        num += abs(ans[i] - ans[i+1])
    return num

def backtrack():
    global answer
    if len(ans) == n:
        answer = max(answer, count())
        return
    
    for i in range(n):
        if used[i]:
            used[i] = False
            ans.append(numbers[i])
            backtrack()
            ans.pop()
            used[i] = True
            
backtrack()    
print(answer)