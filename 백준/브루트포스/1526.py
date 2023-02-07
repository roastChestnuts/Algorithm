gold_list = [7, 4]
gold_check = 0

n = int(input())

for i in range(n, 3, -1):
    for num in str(i):
        if int(num) not in gold_list:
            gold_check = 1
            break
        gold_check = 0
    if gold_check == 0:
      print(i)
      break
    