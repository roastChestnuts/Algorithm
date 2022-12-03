from collections import deque

n,m = map(int, input().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0]*m for _ in range(n)]

def bfs(x, y):
  q = deque()
  q.append([x,y])
  visited[x][y] = 1
  area = 1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if visited[nx][ny] == 1 or graph[nx][ny] == 0:
        continue
      visited[nx][ny] = 1
      q.append([nx, ny])
      area = area + 1
  return area    
      
for i in range(n):
  graph.append(list(map(int, input().split())))

count = 0 #그림의 개수
area = 0 #그림의 넓이

for i in range(n):
  for j in range(m):
    if visited[i][j] == 0 and graph[i][j] == 1:
      area = max(area, bfs(i, j))
      count = count+1

print(count)
print(area)