#22.12.15
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0]*m for i in range(n)]
visited = [[0]*m for i in range(n)]
ans = 0
count = 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for i in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

def dfs(x, y):
    global count
  
    if x<0 or y<0 or x>=n or y>=m:
        return
    if graph[x][y] == 0 or visited[x][y] == 1:
        return
    visited[x][y] = 1
  
    count = count+1
  
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        dfs(nx, ny)
    return count
        
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            count = 0
            ans = max(dfs(i, j), ans)
print(ans)            

###################

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0]*m for i in range(n)]

for i in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1 #입력값이 리스트의 인덱스값들보다 1씩 크니까 -1
    
def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m: #그래프의 범위를 벗어나면 리턴
        return 0
    if graph[x][y] == 0:  #쓰레기가 없어도 리턴
        return 0
    graph[x][y] = 0  #쓰레기 카운트 -> 0으로 변경
    global count
    count += 1  #쓰레기 +1
  
    dfs(x+1, y) #아래
    dfs(x-1, y) #위
    dfs(x, y+1) #우
    dfs(x, y-1) #좌
  
    return count

ans = 0
count = 0
for i in range(n):
    for j in range(m):
        count=0 #카운트 초기화
        ans=max(ans, dfs(i,j))
        
print(ans)        