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