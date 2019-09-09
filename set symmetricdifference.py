a, b, c, d = int(input()), set(map(int, input().split())), input(), set(map(int, input().split()))
print(len(b.symmetric_difference(d)))