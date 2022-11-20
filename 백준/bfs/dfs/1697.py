from collections import deque

n, k = map(int, input().split())
graph = [-1 for _ in range(100001)]
dx = [-1, 1, 2]
graph[n] = 0

def bfs(node):
  q = deque()
  q.append(node)
  while q:
    node = q.popleft()
    for i in range(3):
      if i == 2:
        nx = node*2
      else:
        nx = node+dx[i]
      if nx >= 0 and nx <= 100000:
        if graph[nx] == -1:
          graph[nx] = graph[node] + 1
          q.append(nx)
bfs(n)
print(graph[k])         