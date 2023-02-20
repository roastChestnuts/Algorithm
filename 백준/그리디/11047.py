import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coin_arr = []
count = 0

for i in range(n):
    coin_arr.append(int(input()))
coin_arr.sort(reverse=True)

for coin in coin_arr:
    if k == 0:
        break
    if coin <= k:
        count += k//coin
        k %=coin
print(count)


###########################

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coin_list = []
count = 0

for i in range(n):
    coin_list.append(int(input()))
coin_list.sort(reverse=True)

for coin in coin_list:
    if k == 0:
        break
    if coin <= k:
        count += k//coin
        k %=coin
print(count)