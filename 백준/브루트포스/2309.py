import sys
input = sys.stdin.readline

arr = []
for i in range(9):
    arr.append(int(input()))

check_sum = sum(arr)

del_1=0
del_2=0

for i in range(8):
    for j in range(i+1, 9):
        if check_sum-arr[i]-arr[j] == 100:
            del_1 = arr[i]
            del_2 = arr[j]
            break

arr.remove(del_1)          
arr.remove(del_2)
arr.sort()
for num in arr:
    print(num)