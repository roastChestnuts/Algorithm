n = int(input())
min = 0
max = 0

numbers = list(map(int,input().split()))

numbers.sort()
min = numbers[0]
max = numbers[-1]
print(min, max)            