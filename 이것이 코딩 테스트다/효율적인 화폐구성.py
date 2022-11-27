n, m = map(int, input().split())
coin_list = [0] * n
for i in range(n):
    coin_list[i] = int(input())

dp = [10001] * (m+1)
dp[0] = 0

for coin in coin_list:
    for i in range(coin, m+1):
        if dp[i-coin] != 10001:
            dp[i] = min(dp[i-coin]+1, dp[i])

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])