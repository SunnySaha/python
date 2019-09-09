import numpy

a, b = map(int,input().split())
c = numpy.array([input().split() for _ in range(a)], int)
d = numpy.array([input().split() for _ in range(a)], int)

print(c+d)
print(c-d)
print(c*d)
print(c//d)
print(c%d)
print(c**d)
