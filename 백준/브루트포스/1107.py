import sys

current_c = 100
target_c = int(sys.stdin.readline())
broken_count = int(sys.stdin.readline())
minimum = abs(current_c - target_c)

if broken_count:
    broken_buttons = set(sys.stdin.readline().split())
else:
    broken_buttons = set()
    
for i in range(1000001):
    for num in str(i):
        if num in broken_buttons:
            break
    else:
        minimum = min(minimum, len(str(i)) + abs(i - target_c))
print(minimum)            
