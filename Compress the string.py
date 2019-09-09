from itertools import groupby
print(*[(len(list(j)), int(i)) for i , j in groupby(input())])