n = int(input())
numbers = [1 for _ in range(n)]
result = [num if i % 2 == 0 else num + 1 for i, num in enumerate(numbers)]

if n%2 == 1:
  result[-1] = 3
print(*result)  
       