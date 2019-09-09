import numpy
a = int(input())
arr = numpy.array([input().split() for _ in range(a)], int)
arr2 = numpy.array([input().split() for _ in range(a)], int)
print(numpy.dot(arr, arr2))