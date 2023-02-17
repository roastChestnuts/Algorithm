while True:
  try:
      n, m = map(int, input().split())
  except:
      break
  answer = 0

  for i in range(n, m+1):
      check = str(i)
      flag = True
      for j in check:
          if check.count(j) > 1:
              flag = False
              break
      if flag:
          answer += 1
  print(answer)      