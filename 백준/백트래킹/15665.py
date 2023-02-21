n, m = map(int, input().split())
numbers = list(set(map(int, input().split())))
numbers.sort()
answer = []

def backtrack():
    if len(answer) == m:
        print(*answer)
        return
    
    for number in numbers:
        answer.append(number)
        backtrack()
        answer.pop()
backtrack()