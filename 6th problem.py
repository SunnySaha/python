import math

c = 50
h = 30
d = [x for x in input().split(',')]

li = []

for i in d:
    li.append(str(int(round(math.sqrt(2*c*float(i)/h)))))


print(','.join(li))