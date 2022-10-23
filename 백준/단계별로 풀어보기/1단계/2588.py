a = int(input())
b = int(input())
c = a * b


print(a*(b%10))
print(a*((b%100)//10))
print(a*((b%1000)//100))
print(c)