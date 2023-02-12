numbers = list(map(int, input().split()))

for i in range(1000000):
    count = 0
    for num in numbers:
        if i >= num:
            if i % num == 0:
                count += 1
    if count >= 3:
        print(i)
        break