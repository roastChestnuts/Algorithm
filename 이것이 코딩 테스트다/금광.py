for tc in range(int(input())) :
  n, m = map(int, input().split())
  arr = list(map(int, input().split()))
  dp = []
  index = 0
  for i in range(n) :
    dp.append(arr[index: index + m])
    index += m

  for j in range(1, m) :
    for i in range(n) :
      if i == 0:
        left_up = 0
      else :
        left_up = dp[i - 1][j - 1]

      if i == n - 1 :
        left_down = 0
      else :
        left_down = dp[i + 1][j - 1]

      left = dp[i][j - 1]
      dp[i][j] = dp[i][j] + max(left_up, left_down, left)

  result = 0
  for i in range(n) :
    result = max(result, dp[i][m - 1])
  print(result)


#####################################
for tc in range(int(input())) :
  n, m = map(int, input().split())
  arr = list(map(int, input().split()))
  gold_list = []
  
  for i in range(0, n*m, m) :
    gold_list.append(arr[i: i+m])

  for j in range(1, m) :
    for i in range(n) :
      left_up, left_down, left = 0, 0, 0
      if i != 0:
        left_up = gold_list[i - 1][j - 1]
      if i != (n - 1) :
        left_down = gold_list[i + 1][j - 1]
      left = gold_list[i][j - 1]
      gold_list[i][j] = gold_list[i][j] + max(left_up, left_down, left)

  result = 0
  for i in range(n) :
    result = max(result, gold_list[i][m - 1])
  print(result)