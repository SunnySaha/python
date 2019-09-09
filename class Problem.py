class check:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        return self.s.upper()


obj = check()

obj.getString()

print(obj.printString())