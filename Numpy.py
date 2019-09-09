import numpy

def arrays(arr):
   return numpy.array(arr[::-1], float)

arr = input().split(' ')
result = arrays(arr)
print(result)