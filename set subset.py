
for _ in range(int(input())):
    n, a, m , b = input(), set(map(int, input().split())), input(), set(map(int, input().split()))
    if (b.intersection(a)==a):
        print("True")
    else:
        print("False")