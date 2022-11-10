#괄호를 추가할 때 선언적 사고를 하지못해 애를먹었다
#재귀를 풀다가 막히면 항상 선언적사고를 하자..!!!!
import sys
input = sys.stdin.readline

ans = []
n = int(input())
data_list = []

for i in range(n):
    data_list.append(list(map(int,input().rstrip())))

def recur(x, y, n):
    global ans
    color = data_list[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != data_list[i][j]:
                ans.append('(') #분할되면 괄호를 씌워줘야 한다.
                recur(x, y, n//2)
                recur(x, y+n//2, n//2)
                recur(x+n//2, y, n//2)
                recur(x+n//2, y+n//2, n//2)
                ans.append(')') #분할이 끝났으면 괄호를 닫아준다.
                return
    ans.append(color) #분할되지 않았으면 그냥 추가해준다.
  
recur(0,0,n)  
print(''.join(map(str,ans)))