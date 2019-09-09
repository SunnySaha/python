from itertools import combinations

str , n = input().split()

print(*[''.join(i) for x in range(1, int(n)+1) for i in combinations(sorted(str), x)], sep='\n')