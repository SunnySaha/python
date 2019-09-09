from collections import Counter, OrderedDict


class result(Counter, OrderedDict):
    pass


[print(*c) for c in result(sorted(input())).most_common(3)]