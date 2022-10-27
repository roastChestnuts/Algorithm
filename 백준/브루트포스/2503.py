num_list = [True for i in range(1000)]

for i in range(123, 1000):
  list_i = str(i)
  if list_i[0] == list_i[1] or list_i[1] == list_i[2] or list_i[0] == list_i[2]:
    num_list[i] = False
  elif list_i[0] == '0' or list_i[1] == '0' or list_i[2] == '0':
    num_list[i] = False

n = int(input())

for i in range(n):
  hint, s, b = map(int, input().split())
  hint = str(hint)
  
  for num in range(123, 1000):
    chk_s, chk_b = 0, 0
    if num_list[num]:
      str_num = str(num)
      for j in range(3):
        for k in range(3):
          if str_num[j] == hint[k] and j == k:
            chk_s += 1
          elif str_num[j] == hint[k] and j != k:
            chk_b += 1
      if chk_b == b and chk_s == s:
        num_list[num] = True
      else:
        num_list[num] = False

cnt=0
for i in range(123,1000):
  if num_list[i]:
    cnt+=1
print(cnt)        