from math import *
import math


class metrix:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def dot(self, other):
        s, o = self, other
        return s.x * o.x + s.y * o.y + s.z * o.z

    def cross(self, other):
        return metrix(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def mod(self):
        return pow(self.x**2+ self.y**2+ self.z**2, 0.5)

    def __sub__(self, other):
        return metrix(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        return metrix(self.x + other.x, self.y + other.y, self.z + other.z)

def initial():
    return metrix(*map(float, input().split()))

if __name__ == "__main__":
    A = initial()
    B = initial()
    C = initial()
    D = initial()
    AB = B - A
    BC = C - B
    CD = D - C
    X = AB.cross(BC)
    Y = BC.cross(CD)
    print("%0.2f" %math.degrees(math.acos(X.dot(Y) / X.mod() / Y.mod())))
