from collections import Counter, OrderedDict

wordDict = OrderedDict()

for _ in range(int(input())):
    word = input()
    wordDict.setdefault(word, 0)
    wordDict[word] += 1
print(len(wordDict))
print(*wordDict.values())