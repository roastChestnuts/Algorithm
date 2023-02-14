n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
root = []
answer = 1e9

def check():
    cost = 0
    
    for i in range(n):
        _from = root[i]
        if i == (n-1):
            _to = root[0]
        else:
            _to = root[i+1]
        if graph[_from][_to] == 0:
            return 1e9
        cost += graph[_from][_to]
    return cost

def backtrack():
    global answer
    if len(root) == n:
        answer = min(answer, check())
        return
    for i in range(n):
        if i not in root:
            root.append(i)
            backtrack()
            root.pop()
backtrack()
print(answer)