n = int(input())
board = [list(input()) for _ in range(n)]
answer = 0

def check_row():
  global answer
  #행 최대개수 체크
  for i in range(n):
    count = 1
    for j in range(n-1):
        if board[i][j] == board[i][j+1]:
            count += 1
        else:
            count = 1
        answer = max(answer, count)
        
def check_col():
  global answer
  #열 최대개수 체크
  for i in range(n):
    count = 1
    for j in range(n-1):
        if board[j][i] == board[j+1][i]:
            count += 1
        else:
            count = 1
        answer = max(answer, count)

for i in range(n):
    for j in range(n - 1):
        #열 체크
        if board[i][j] != board[i][j + 1]:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            check_row()
            check_col()
            board[i][j + 1], board[i][j] = board[i][j], board[i][j + 1]
        #행 체크
        if board[j][i] != board[j + 1][i]:
            board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]
            check_row()
            check_col()
            board[j + 1][i], board[j][i] = board[j][i], board[j + 1][i]
            
print(answer)            