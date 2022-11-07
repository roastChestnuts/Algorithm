n = int(input())
m = n
count = 0
  
while True:
    remain = n % 10
    n = (n//10) + (n%10)
    n = int(str(remain) + str(n % 10))
    count += 1
    if(n == m):
      break
    
print(count)    