for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError as f:
        print("Error Code:", f)
    except ValueError as f:
        print("Error Code:", f)
