def O3n(n):
    x = 0
    for i in range(3):
        for j in range(n):
            x = x + 1
    return x

def Onlogn(n):
    x = 0
    for i in range(n):
        j = n
        while j >= 1:
            x = x + 1
            j = int(j / 2)
    return x

def OnF(n):
    x = n
    if n == 0:
        return 1
    for i range(n):
        x = n * OnF(n-1)
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
        j = n
        while j >= 1:
            x = x + 1
            j = int(j / 2)
    return x
