from collections import deque

q=deque()
m,n=map(int,input().split())
graph=[]
dx,dy=[1,-1,0,0], [0,0,1,-1]
ans = 0

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] != 0 :
                continue
            graph[nx][ny] = graph[x][y] + 1
            q.append([nx, ny])

for i in range(n):
    graph.append(list(map(int,input().split())))
    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i,j])
bfs()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
        ans = max(ans, graph[i][j])    
print(ans-1)            