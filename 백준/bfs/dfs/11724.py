import sys
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    for near in graph[node]:
        if visited[near] == False:
            dfs(near)
          
v,e = map(int, input().split())
graph = [[] for i in range(v+1)]
visited = [False for i in range(v+1)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

for i in range(v+1):
  graph[i].sort()
  
count = 0 
for i in range(1, v+1):
  if visited[i] == False:
    dfs(i)
    count+=1
        
print(count)        