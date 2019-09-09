n, m = input(), set(map(int, input().split()))

for _ in range(int(input())):
    li = list(input().split())
    if 'intersection_update' in li:
        k = set(map(int, input().split()))
        m.intersection_update(k)

    if 'update' in li:
        k = set(map(int, input().split()))
        m.update(k)

    if 'symmetric_difference_update' in li:
        k = set(map(int, input().split()))
        m.symmetric_difference_update(k)

    if 'difference_update' in li:
        k = set(map(int, input().split()))
        m.difference_update(k)
print(sum(m))