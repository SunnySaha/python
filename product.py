from itertools import product

li = ['su', 'dh', 'sr']

m = list(product(*li))
print(m)