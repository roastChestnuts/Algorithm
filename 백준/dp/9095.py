import sys
input = sys.stdin.readline

n = int(input()) #입력횟수

ans = [0] * 12 #배열초기화
ans[1] = 1
ans[2] = 2
ans[3] = 4

for i in range(4, 12):
    ans[i] = ans[i-1] + ans[i-2] + ans[i-3] #점화식

for i in range(n):
    idx = int(input())
    print(ans[idx])
    