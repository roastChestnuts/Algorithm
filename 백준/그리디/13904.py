import sys
input = sys.stdin.readline

n = int(input())
assign_list = []
max_list = [0 for i in range(1001)]
for i in range(n):
    assign_list.append(list(map(int, input().split())))
assign_list.sort(reverse=True, key=lambda x: x[1])

for i in range(n):
    j = assign_list[i][0]
    for k in range(j, 0, -1):
        if max_list[k] == 0:
            max_list[k] = assign_list[i][1]
            break
print(sum(max_list))            