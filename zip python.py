mark = []

x, n = map(int, input().split())

for _ in range(n):
    mark.append(map(float, input().split()))

for i in zip(*mark):
    print(sum(i)/n)