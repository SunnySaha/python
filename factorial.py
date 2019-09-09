def fact(value):
    if (value == 0):
        return 1;
    else:
       return value * fact(value-1)



x = int(input())
print((fact(x)))