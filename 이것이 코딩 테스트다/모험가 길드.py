n = int(input())
x = list(map(int, input().split()))
ans = 0 #총 파티 수
count = 0 #파티원 체크

x.sort()

for i in x:
    count += 1
    if count >= i:
        ans += 1
        count = 0
print(count)        