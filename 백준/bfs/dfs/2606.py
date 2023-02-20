from collections import deque

v = int(input())
e = int(input())
graph = [[] for i in range(v+1)]
visited = [False] * (v+1)
count = 0

for i in range(e):
  a, b = map(int, input().split())
  graph[a] += [b]
  graph[b] += [a]

def bfs(node):
  global count
  q = deque()
  q.append(node)
  while q:
    node = q.popleft()
    if visited[node] == False:
      visited[node] = True
      q.extend(graph[node])
      count += 1

bfs(1)
print(count-1)