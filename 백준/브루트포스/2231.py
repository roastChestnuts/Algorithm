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


# constructor = 0
# num = int(input())

# for n in range(num):
#     constructor = n
#     for j in str(n):
#         constructor += int(j)
#     if constructor == num:
#         constructor = n
#         break
#     else:
#         constructor = 0
# print(constructor)        