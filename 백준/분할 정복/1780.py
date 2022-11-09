import sys
input = sys.stdin.readline

num = int(input())
paper = []
ans = []

for i in range(num):
    paper.append(list(map(int, input().split())))
    
def recur(x, y, n):
    nst = n//3
    check_num = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check_num != paper[i][j]:
                recur(x, y, nst)
                recur(x, y+nst, nst)
                recur(x, y+nst*2, nst)
                recur(x+nst, y, nst)
                recur(x+nst, y+nst, nst)
                recur(x+nst, y+nst*2, nst)
                recur(x+nst*2, y, nst)
                recur(x+nst*2, y+nst, nst)
                recur(x+nst*2, y+nst*2, nst)
                return
    ans.append(check_num)


recur(0,0,num)
print(ans.count(-1))
print(ans.count(0))
print(ans.count(1))