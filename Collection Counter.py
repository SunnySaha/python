from collections import Counter


x = int(input())

li = Counter(map(int, input().split()))

N = int(input())

amount =0

for i in range(N):
    size, price = map(int, input().split())

    if li[size]:
        amount += price
        li[size] -=1


print(amount)