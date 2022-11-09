import sys
input = sys.stdin.readline

n = int(input())
paper = [] #색종이
ans = [] #답

for i in range(n):
    paper.append(list(map(int, input().split())))
     
def recur(x, y, n):    
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                recur(x,y,n//2)
                recur(x,y+n//2,n//2)
                recur(x+n//2,y,n//2)
                recur(x+n//2,y+n//2,n//2)
                return
    ans.append(color)

recur(0,0,n)
print(ans.count(0))
print(ans.count(1))