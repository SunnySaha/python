str, n = input(), int(input())

for i in zip(*[iter(str)]*n):
    dic = dict()
    print(''.join([dic.setdefault(c, c) for c in i if c not in dic]))

