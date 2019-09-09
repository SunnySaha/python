from itertools import combinations_with_replacement as cp

str, n = input().split()

print(*[''.join(i) for i in cp(sorted(str), int(n))], sep='\n')