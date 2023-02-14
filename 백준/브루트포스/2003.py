#투포인터 기본문제
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
count = 0
interval_sum = 0
end = 0

for i in range(n):
    while interval_sum < m and end < n:
        interval_sum += numbers[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= numbers[i]
            
print(count)            