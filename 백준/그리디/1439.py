numbers = list(input())
start = numbers[0]
summary = [start]

for i in range(1, len(numbers)):
    if start != numbers[i]:
        start = numbers[i]
        summary.append(start)
print(min(summary.count('0'), summary.count('1')))    