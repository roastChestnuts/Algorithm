x, y = 1, 1
n = int(input())
moves = list(input().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
types = ['L', 'R', 'U', 'D']

for move in moves:
    for i in range(len(types)):
        if move == types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx > n or ny > n or nx < 1 or ny < 1:
        continue
    x = nx
    y = ny

print(x, y)    