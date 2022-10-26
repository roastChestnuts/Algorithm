tri_num = [ (i*(i+1))//2 for i in range(1, 45) ] # 대략 45정도의 삼각수라면 1000을 넘거나 근접하기때문에 이 이상은 구할 필요가 없다.

n = int(input())

for i in range(n):
    check = int(input())
    answer = 0
    for j in range(44): 
      if answer == 1: break
      for k in range(44):
        if answer == 1: break
        for l in range(44):
          if tri_num[j] + tri_num[k] + tri_num[l] == check:
            answer = 1
            break
    print(answer)       
