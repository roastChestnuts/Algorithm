import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coin_arr = [0]*n
count = 0

for i in range(n):
    coin_arr.append(int(input()))
coin_arr.sort(reverse=True)

for coin in coin_arr:
    if k == 0:
        break
    if coin <= k:
        count += k//coin
        k = k%coin
print(count)