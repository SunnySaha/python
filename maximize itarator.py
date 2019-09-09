from itertools import product

n , m = [int(i) for i in input().split()]

li = []

for _ in range(n):
    li.append([int(x) for x in input().split()][1:])


combinations = list(product(*li))

def val(self):
    return sum(i*i for i in self)%m

print(max(list(map(val, combinations))))
