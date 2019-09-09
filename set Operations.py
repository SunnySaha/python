n, m = int(input()), set(map(int, input().split()))
for _ in range(0,int(input())):
    li = list(input().split())
    if 'pop' in li:
        m.pop()

    if 'discard' in li :
        m.discard(int(li[1]))
    if 'remove' in li:
        m.remove(int(li[1]))
print(sum(m))
