ls = [True for i in range(1000001)]
ls[0] = False
ls[1] = False
m = 1000000

for i in range(2, int(m ** 0.5)):
    j = 2
    if ls[i] == True:
        while i*j <= m:
            ls[i*j] = False
            j += 1
            
n = int(input())
even_list = []
for i in range(n):
    even_list.append(int(input()))

  

for even in even_list:
  count = 0
  for i in range(2, even//2+1):
    if ls[i] and ls[even-i]:
      count+=1
  print(count)            