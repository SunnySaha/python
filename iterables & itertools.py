from itertools import combinations

_, li, n = input(), input().split(), int(input())

it = list(combinations(li, n))

result = [i for i in it if 'a' in i]

print(it)
print(len(result)/len(it))