import sys
input = sys.stdin.readline

n = int(input())
lope = []
ans = 0
for i in range(n):
  lope.append(int(input()))
lope.sort()  

for i in range(n):
  ans = max(ans, lope[i]*(n-i))

print(ans)
  