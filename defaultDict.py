from collections import defaultdict

n, m = map(int, input().split())
li = []
d = defaultdict(list)

for i in range(0, n):
    d[input()].append(i+1)

for i in range(0, m):
    li = li+[input()]

for i in li:
    if i in d:
        print(" ".join(map(str, d[i])))
    else:
        print("-1")