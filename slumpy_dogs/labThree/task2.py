def O3n(n):
    x = 0
    for i in range(3):
        for j in range(n):
            x = x + 1
    return x

def Onlogn(n):
    x = 0
    for i in range(n):
        j = int(n / 2)
        while j >= 1:
            for k in range(j):
                x = x + 1
            j = int(j / 2)
    return x

def OnF(n):
    x = 0
    z = 1
    for i in range(1, n + 1):
        z *= i
    for i in range(z):
        x = x + 1
    return x

def On3(n):
    x = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                x = x + 1
    return x

def O3logn(n):
    x = 0
    for i in range(3):
        j = int(n / 2)
        while j >= 1:
            for k in range(j):
                x = x + 1
            j = int(j / 2)
    return x


