#풀리는데 느리다.. 개선점이 필요
answer = 1e9
n = int(input())
recipes = [list(map(int, input().split())) for _ in range(n)]
use = [True for _ in range(n)]

def check():
  sour = 1
  bitter = 0
  for i in range(n):
    if use[i] == False:
      sour *= recipes[i][0]
      bitter += recipes[i][1]
  return abs(sour-bitter)

def backtrack(depth):
  global answer
  
  if depth > n:
    return
  if depth > 0:
    answer = min(answer, check())

  for i in range(n):
    if use[i] == True:
      use[i] = False
      backtrack(depth+1)
      use[i] = True

backtrack(0)
print(answer)

#2번 풀이
import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

answer = 1e9
n = int(input())
recipes = [list(map(int, input().split())) for _ in range(n)]


def backtrack(depth, sour, bitter):
  global answer
  
  if depth == n:
    #쓴 맛이 0 이라면 아무것도 사용하지 않은 경우이기에 제외해야함
    if bitter != 0:
      answer = min(answer, abs(sour-bitter))
    return
  backtrack(depth+1, sour, bitter)  
  backtrack(depth+1, sour*recipes[depth][0], bitter+recipes[depth][1])  
    

backtrack(0, 1, 0)
print(answer)