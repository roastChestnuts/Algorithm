n = int(input())
visited_1 = [0] * 15 #세로 열 가능여부
visited_2 = [0] * 30 #좌하단 대각선 열 가능여부
visited_3 = [0] * 30 #우하단 대각선 열 가능여부
ans = 0 # 정답개수

def n_queen(row):
  global ans
  if row == n:
    ans = ans+1
    return
  for i in range(n): #n개의 열을 돌면서
    if visited_1[i] or visited_2[i+row] or visited_3[i-row+n]:
      continue
    visited_1[i] = 1
    visited_2[i+row] = 1
    visited_3[i-row+n] = 1
    n_queen(row+1) #다음 열 탐색
    visited_1[i] = 0
    visited_2[i+row] = 0
    visited_3[i-row+n] = 0

n_queen(0)      
print(ans)
