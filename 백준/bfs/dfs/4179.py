from collections import deque

r, c = map(int,input().split()) #행, 열 입력
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1] #상하좌우
graph = [] #그래프
ji = [[-1]*c for i in range(r)] #지훈이 탈출 그래프
fire = [[-1]*c for i in range(r)] #불길 그래프

q1 = deque() #지훈이 탐색용
q2 = deque() #불길 탐색용

for i in range(r):
  graph.append(list(map(str,input()))) #그래프 입력


for i in range(r):
  for j in range(c):
    if graph[i][j] == 'J': #지훈이가 서있는 곳
      ji[i][j] = 0 #0으로 초기화
      q1.append([i, j]) #q1 에 append
    if graph[i][j] == 'F':
      fire[i][j] = 0
      q2.append([i, j]) 

#불길 탐색(각 지점별 거리 계산)
def f_bfs():
  while q2:
    x, y = q2.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= r or ny >= c:
        continue
      if graph[nx][ny] == '#' or fire[nx][ny] >= 0: #벽이면 컨티뉴
        continue
      fire[nx][ny] = fire[x][y] + 1
      q2.append([nx, ny])

#지훈이 탐색
def ji_bfs():
  while q1:
    x, y = q1.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= r or ny >= c: #상 하 좌 우 어디든 탈출을 성공했다면
        print(ji[x][y]+1)
        return
      if graph[nx][ny] == '#' or ji[nx][ny] >= 0:
        continue
      if fire[nx][ny] != -1 and fire[nx][ny] <= ji[x][y] + 1: #불길이 번진 속도가 지훈이 보다 빠르다면
        continue
      ji[nx][ny] = ji[x][y] + 1
      q1.append([nx, ny])
  print('IMPOSSIBLE') #while문을 탈출했다면 지훈이가 탈출하지 못했으니

f_bfs()
ji_bfs()

