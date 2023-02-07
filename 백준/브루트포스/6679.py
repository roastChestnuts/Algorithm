def conversion(num, arithmetic):
  sum = 0
  while num > 0:
    sum += num % arithmetic
    num //= arithmetic
  return sum
  
for i in range(1000, 10000):
    sum_10 = conversion(i, 10)
    sum_12 = conversion(i, 12)
    sum_16 = conversion(i, 16)
  
    if sum_10 == sum_12 and sum_12 == sum_16:
      print(i)