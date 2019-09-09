from collections import deque

for _ in range(int(input())):
    input()
    check = deque(map(int, input().strip().split()))
    result = "Yes"
    if max(check) not in (check[0],check[-1]):
        result = "No"
    print(result)