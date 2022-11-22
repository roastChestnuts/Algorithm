import sys
sys.setrecursionlimit(100000)
n = int(input())
graph = []
ans = []

for i in range(n):
  graph.append(list(map(str, input())))

def dfs(x, y, color):
  if x < 0 or y < 0 or x >= n or y >= n:
    return False
  if graph[x][y] != color:
    return False
  if visited[x][y] == False:
    visited[x][y] = True
    dfs(x+1, y, color)
    dfs(x-1, y, color)
    dfs(x, y+1, color)
    dfs(x, y-1, color)
    return True
  return False

def color_change(graph):
  for i in range(n):
    for j in range(n):
      if graph[i][j] == 'G':
        graph[i][j] = 'R'

for i in range(2):
  count = 0
  visited = [[False]*n for _ in range(n)]
  for j in range(n):
    for k in range(n):
      if visited[j][k] == False:
        color = graph[j][k]
        count += 1
        dfs(j, k, color)
  color_change(graph)        
  ans.append(count)        
print(*ans)