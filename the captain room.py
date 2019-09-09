
n, m = int(input()), list(map(int, input().split()))
s = set(m)
print((sum(s)*n - sum(m))//(n-1))
