n,m = map(int, input().split())
board = []
min_ = []

for i in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        b_count, w_count = 0, 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 0:
                    if board[k][l] != 'B':
                        b_count +=1
                    else:
                        w_count +=1
                else:
                    if board[k][l] != 'W':
                        b_count +=1
                    else:
                        w_count +=1
        min_.append(min(w_count, b_count))
print(min(min_))