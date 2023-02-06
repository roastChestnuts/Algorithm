#시간 복잡도 O(n)
import sys
input = sys.stdin.readline

constructor = 0
num = int(input())

for n in range(num):
     #문자열을 list로 변환하면 각 요소들이 하나의 리스트 멤버가된다.
    if n + sum(list(map(int, str(n)))) == num:
        constructor = n
        break

print(constructor)           
