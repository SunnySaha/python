from itertools import  permutations as pm

str, n = input().split()

print(*[''.join(i) for i in pm(sorted(str), int(n))], sep='\n')