import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [0] + list(map(int, input().split()))
dp = [0]*(n+1)

dp[1] = array[1]

for i in range(2, n+1):
  dp[i] = dp[i-1] + array[i]

for i in range(m):
  i, j = map(int, input().split())
  if i == 1:
    print(dp[j])
  else:
    print(dp[j]-dp[i-1])