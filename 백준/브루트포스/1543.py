target = input()
search = input()
answer = 0
idx = 0
plus = len(search)

for i in range(len(target)):
    if idx+plus <= len(target) and target[idx:idx+plus] == search:
        idx += plus
        answer += 1
    else:
        idx += 1
print(answer)        