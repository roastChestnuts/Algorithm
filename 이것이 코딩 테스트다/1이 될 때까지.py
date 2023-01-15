#내 풀이
n, k = map(int, input().split())
count = 0

while(n != 1):
    if(n%k == 0):
        count += 1
        n //= k
    else:
        count += 1
        n -= 1
print(count)

#답안 풀이
n, k = map(int, input().split())
count = 0

while True:
    target = (n//k)*k 
    count += n - target #ex 27, 4 => count 3추가 //// 위의 풀이에서처럼 3번을 반복하지 않고 한번에 값을 계산 해낼 수 있음
    n = target
    if n < k: #더 이상 나눌 수 없다면 탈출
        break

    count += 1
    n //= k

count += (n-1) #혹시 n이 1이 아닌 상태로 더 이상 나눌 수 없어서 탈출한 거라면 n-1만큼의 횟수를 더해준다.
print(count)
