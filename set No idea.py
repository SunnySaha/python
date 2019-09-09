n, m = input().split()

arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
#print (sum([(i in a) - (i in b) for i in arr]))
h=0
for i in arr:
    if i in a:
        h+=1
    if i in b:
        h-=1

print(h)