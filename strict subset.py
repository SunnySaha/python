a = set(map(int, input().split()))
n = int(input())
flag =0;
for _ in range(1, n+1):
    b = set(map(int, input().split()))
    if(b.intersection(a)==b and len(a)>len(b)):
        flag +=1
    else:
        flag -=1

if n == flag:
    print("True")
else:
    print("False")