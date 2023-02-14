n = list(input())
answer = -1

if sum(map(int, n)) % 3 == 0 and '0' in n:
    answer = 0

if answer == 0:
    n.sort(reverse=True)
    print(''.join(n))
else:
    print(answer)
    