from collections import OrderedDict

n = int(input())
order_dict = OrderedDict()
for _ in range(n):
    item, space, price = input().rpartition(' ')
    order_dict[item] = order_dict.get(item, 0) + int(price)
for val, price in order_dict.items():
    print(val, price)