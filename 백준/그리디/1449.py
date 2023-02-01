n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
count = 1
l_ = l-1

for i in range(1,n):
    if arr[i] - arr[i-1] <= l_:
        l_ -= arr[i] - arr[i-1]
    else:
        count +=1
        l_ = l-1
print(count)        
###########################230202 다시
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
pipe = list(map(int, input().split()))
pipe.sort()
count = 1
start = pipe[0]

for i in range(1, n):
    if pipe[i]-start > l-1:
        count += 1
        start = pipe[i]
print(count)
