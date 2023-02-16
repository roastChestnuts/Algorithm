n = int(input())
coin = [int(input()) for _ in range(n)]

coin.sort(reverse=True)

answer = 0
for i in range(n):
    tip = coin[i] - i
    if tip >= 0:
      answer += tip
    
print(answer)    