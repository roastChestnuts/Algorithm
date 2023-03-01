import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
ans = []
    
def recur(x, y, n):
    div = n//3
    #시작지점 기준값
    check_num = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check_num != paper[i][j]:
                recur(x, y, div)
                recur(x, y+div, div)
                recur(x, y+div*2, div)
                recur(x+div, y, div)
                recur(x+div, y+div, div)
                recur(x+div, y+div*2, div)
                recur(x+div*2, y, div)
                recur(x+div*2, y+div, div)
                recur(x+div*2, y+div*2, div)
                return
    ans.append(check_num)


recur(0,0,n)
print(ans.count(-1))
print(ans.count(0))
print(ans.count(1))