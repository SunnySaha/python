import re
for _ in range(int(input())):
    r = True
    try:
       rex = re.compile(input())
       print(r)
    except re.error:
        r = False
        print(r)