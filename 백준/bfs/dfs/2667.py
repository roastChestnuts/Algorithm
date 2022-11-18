def dfs(x, y):
  if x<0 or y <0 or x>=n or y >= n:
    return
  if graph[x][y] == 0:
    return
  
  graph[x][y] = 0
  global count
  count += 1
  dfs(x-1, y)
  dfs(x, y-1)
  dfs(x+1, y)
  dfs(x, y+1)

n = int(input())
graph = []

for i in range(n):
  graph.append(list(map(int, input())))

count = 0
ans = []

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      dfs(i, j)
      ans.append(count)
      count = 0

ans.sort()
print(len(ans))
for num in ans:
  print(num)