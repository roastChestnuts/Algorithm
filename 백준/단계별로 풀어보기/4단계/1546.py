import sys
input = sys.stdin.readline

n = int(input())
num_arr = list(map(int, input().split()))
sum = 0

m = max(num_arr)

for num in num_arr:
    sum += num/m*100
print(sum/n)
