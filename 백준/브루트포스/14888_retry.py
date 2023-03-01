import sys

input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
opr = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, tmp, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == n:
        maximum = max(tmp, maximum)
        minimum = min(tmp, minimum)
        return

    if plus:
        dfs(depth + 1, tmp + numbers[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, tmp - numbers[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, tmp * numbers[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(tmp / numbers[depth]), plus, minus, multiply, divide - 1)


dfs(1, numbers[0], opr[0], opr[1], opr[2], opr[3])
print(maximum)
print(minimum)