def average(m):
    s = set(m)
    f = sum(s)/len(s)
    return f


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)