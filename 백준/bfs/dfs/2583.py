import sys
sys.setrecursionlimit(100000)

count = 0
ans = []

m, n, k = map(int, input().split())
graph = [[0] * m for i in range(n)] #문제에서 주어지는 그래프를 우측으로 90도 뒤집어서 생성

for i in range(k):
  x, y, x2, y2 = map(int, input().split())
  for j in range(x, x2):
    for k in range(y, y2):
      graph[j][k] = 1 # 1 = 직사각형 영역

def dfs(x,y):
  if x<0 or y<0 or x >= n or y >= m: #범위 벗어나면 리턴
    return False
  if graph[x][y] == 1: #직사각형 영역이어도 리턴
    return False
  graph[x][y] = 1 #방문한 곳은 색칠을 해주고
  global count
  count +=1 #카운트 및 탐색
  dfs(x+1, y)
  dfs(x-1, y)
  dfs(x, y+1)
  dfs(x, y-1)
  return True

for i in range(n):
  for j in range(m):
    count = 0
    if dfs(i, j):
      ans.append(count)

ans.sort()
print(len(ans))
print(*ans)