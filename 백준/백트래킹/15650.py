n, m = map(int, input().split())
ans = []
def func(start):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(start, n+1):
        if i not in ans:
            ans.append(i)
            func(i+1)
            ans.pop()
func(1)            

###########################################################################

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)] #1~n 리스트
ans = [] #결과 담아서 출력할 리스트

def func(idx):
    if len(ans) == m: 
        print(*ans)
        return
    for i in range(idx, n):
        if arr[i] not in ans:
            ans.append(arr[i])
            func(i+1) #자신보다 작은 값은 이미 처리됐으니 호출은 자신보다 큰 값을 시작점으로
            ans.pop()
func(0)          

#######(230130재풀이)
n, m = map(int, input().split())
arr = []

def back(start):
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(start, n+1):
        arr.append(i)
        back(i+1)
        arr.pop()
        
back(1)       

#https://dogsavestheworld.tistory.com/269