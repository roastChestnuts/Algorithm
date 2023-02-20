n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
dp = [[0]*2 for i in range(n)]

dp[0][0] = array[0]

for i in range(1, n):
    if i == 1:
        dp[i][0] = dp[i-1][0] + array[i]
        dp[i][1] = array[i]
    else:
        dp[i][0] = dp[i-1][1] + array[i]
        dp[i][1] = max(dp[i-2]) + array[i]
        
print(max(dp[n-1]))          

#예시값        10 20 15 25 10 20
#인덱스        [0  1  2  3  4  5]
#dp[][0]       10 30 35 50 65 65 이전계단과 나를 더한 값
#dp[][1]        0 20 25 55 45 75 전전계단과 나를 더한 값
#이전계단과 나를 더할 때에는 계단 세개를 연속해서 밟을 수 없기 때문에
#dp[][1]인덱스의 값과 더해줘야 하고
#전전계단을 밟을 때에는 둘 중 큰 값을 골라주면 된다.