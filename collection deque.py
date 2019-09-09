from collections import deque

i = int(input())
d = deque()
for _ in range(1, i+1):
    li = list(input().split())
    if 'append' in li:
        d.append(int(li[1]))
    if 'appendleft' in li:
        d.appendleft(int(li[1]))
    if 'pop' in li:
        d.pop()
    if 'popleft' in li:
        d.popleft()

print(*d)