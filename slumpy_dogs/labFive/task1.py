from random import randint
print("Введите n:")
n = int(input())
array = [0] * n
zero = 0
one = 0
for i in range(n):
    array[i] = randint(0, 1)
    if array[i] == 0:
        zero += 1
    else:
        one += 1
print(array)
print("Вероятность появления нуля = ", zero / n)
print("Вероятность появления единицы = ", one / n)
for i in range(2, n):
    zeroMax = 0
    oneMax = 0
    countZero = 0
    countOne = 0
    for j in range(n):
        if array[j] == 0:
            countZero += 1
        else:
            countZero = 0
        if countZero >= i:
            zeroMax += 1

        if array[j] == 1:
            countOne += 1
        else:
            countOne = 0
        if countOne >= i:
            oneMax += 1
    if zeroMax > 0:
        print(i, "подряд идущих нулей = ", zeroMax )
        print("Вероятность появления такой цепочки = ", zeroMax/(n - i + 1))
    if oneMax > 0:
        print(i, "подряд идущих единиц = ", oneMax)
        print("Вероятность появления такой цепочки = ", oneMax/(n - i + 1))