from collections import namedtuple

(student, Grade) = int(input()), namedtuple('Grade', input().split())
mark = [int(Grade._make(input().split()).MARKS) for _ in range(student)]
print(sum(mark)/len(mark))

