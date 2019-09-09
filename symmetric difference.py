

a, b, c, d = int(input()), input().split(), input(), input().split()

[print(i) for i in sorted(set(b)^set(d), key=int)]