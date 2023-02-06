#시간 복잡도O(n^4) 인데 내부 2중for문이 64회만 동작이라...2중 for로 봐도될듯
n, m = map(int, input().split())
chess = [input() for _ in range(n)]
answer = 3000

for i in range(n-8+1):
    for j in range(m-8+1):
        #짝수 자리가 'B'일때, 짝수 자리가 'W'일 때
        b_count, w_count = 0, 0
        for k in range(i, i+8):
            for l in range(j, j+8):
              if (k+l) % 2 == 0:
                if chess[k][l] == 'B': #짝수 자리가 W일 때(홀수는 B)
                  w_count += 1
                else: #짝수 자리가 B일 때
                  b_count += 1
              else:
                if chess[k][l] == 'W': #홀수 자리는 B여야 함(짝수는 W)
                  w_count += 1
                else:
                  b_count += 1
              
        answer = min(answer, min(w_count, b_count)) 
                       
print(answer)                      